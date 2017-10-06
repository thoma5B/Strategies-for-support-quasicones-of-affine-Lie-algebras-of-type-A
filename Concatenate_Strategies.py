from collections import defaultdict
import numpy as p
import Quasicone
from Quasicone.Apply_strategy import Apply_strategy
from Quasicone.Weyl_normal import Weyl_normal_form
import pickle


# successful items will then be set to '0'

class MapTree:
    """a singleton class"""
    # successful items will then be set to '0'
    
    list_of_defects, list_of_C_derived, = [], []  # static
    # zeroth index is 0, to get indexation right
    list_of_successful = []
    list_of_C_init = []
    max_no_strategies = 0

    def __init__(self, **kwargs):
        """
        :kwargs: startweight, inputfile, n
        """
        self.n = kwargs['n']
        self.as_tuple = lambda C: tuple(tuple(C[i]) for i in range(self.n))
        # for an nxn-array
        self.startweight = kwargs['startweight']
        inputfile = kwargs['exceptionals']
        if inputfile:
            file = open(inputfile, "r")
            list_of_exceptionals = pickle.load(file)
            file.close()
        else:
            print "no inputfile indicated; use option -i [filename]"

        self.Tree = defaultdict(list)
        self.d_derived = defaultdict(list)
        mu = 0
        for C in list_of_exceptionals:
            C_init = self.as_tuple(C._C)  # quasicone must be hashable when key
            if C_init in self.Tree.keys():
                # print " already contained"
                continue
            self.Tree[C_init].append(False)
            self.Tree[C_init].append([mu])
            self.d_derived[C_init].append([mu])
            MapTree.list_of_defects.append(C.defect)
            MapTree.list_of_C_derived.append(C_init)
            # copy in two lists, in order to easily compare with start configuration
            mu += 1
        MapTree.list_of_C_init = list(MapTree.list_of_C_derived)
        MapTree.max_no_strategies = len([i for i in Quasicone.Strategy.iterator(self.n)])

    def get_Tree_key(self, tree_index):
        for C, index_list in self.Tree.items():
            if tree_index in index_list: return C
        return 0

    def remove_by_value(value, dictionary):
        for k, value in dictionary:
            try:
                del dictionary[self.get_Tree_key(value)]
            except:
                pass
        return

    def mark_path_to_node_successful(self, index_list):
        path_to_node = []
        for tree_index in index_list:
            tree_index = list(tree_index)  # a local copy, to not change function argument
            while tree_index:
                C_success = self.get_Tree_key(tree_index)
                MapTree.list_of_successful.append(C_success)
                try:
                    self.Tree[C_success][0] = True
                except IndexError:
                    self.Tree[C_success].insert(0, 0)
                path_to_node.append(C_success)
                try:
                    MapTree.list_of_C_init.remove(C_success)
                except:
                    pass
                tree_index.pop()
        return path_to_node

    def eliminate_side_branches(self, index_list, d_derived):
        #        for tree_indexlist in self.Tree.values() :
        #            for i, tree_index in enumerate(tree_indexlist):
        #                if tree_index[0] == index[0]:
        #                    del tree_indexlist[i]
        for tree_index in index_list:
            # print tree_index
            tree_index_cp = list(tree_index)
            treeindex_last = tree_index_cp[-1]
            try:
                del d_derived[self.get_Tree_key(tree_index_cp)]
            except:
                pass
            for last in range(treeindex_last):
                tree_index_cp[-1] = last
                C = self.get_Tree_key(tree_index_cp)
                try:
                    del d_derived[C]
                except:
                    pass
                MapTree.list_of_defects[tree_index_cp[0]] = 0
                # dont delete to keep list indices in sync
                # tree_index_cp.pop()
        return

    def eliminate_children(self, index_list, d_derived):
        for index in index_list:  # eliminate complete branch
            index.append(0)
            for i in range(MapTree.max_no_strategies):
                index[-1] = i
                C = self.get_Tree_key(index)
                if C == 0: continue
                try:
                    del d_derived[C]
                except:
                    pass
        return

        # 4 cases

    # 1. leaf.defect == 0
    # 1.a. side tree has reduction in balance
    #
    # 2. leaf.balance reduced
    # 2.a. side tree

    # 3. leaf is in list of successful ("coming from top" in picture)
    # 4. one node of the eliminated subtree occurs somewhere else
    #   in the current tree ("coming from bottom" in picture)

    # map of the set of node in the graph of concatenate strategies


    def strategy_step(self):
        d_derived = defaultdict(list)
        # print self.d_derived
        nothing_new = True
        for C, index_list in self.d_derived.items():
            # makes a copy of self.d_derived - modifications manifest only after termination
            for nu, strg in enumerate(Quasicone.Strategy.iterator(self.n)):
                new_instance = Apply_strategy(startweight=self.startweight,
                                              quasicone=p.array(C),
                                              list_of_operators=strg)
                C_der_nor = self.as_tuple(Weyl_normal_form(new_instance.C_derived))
                # 3. ###############################################################
                if new_instance.successful or (C_der_nor in MapTree.list_of_successful):
                    # print C_der_nor, " defect: ", new_instance.defect
                    # print index_list
                    self.eliminate_side_branches(index_list, d_derived)
                    self.mark_path_to_node_successful(index_list)
                    try:
                        self.Tree[C_der_nor][0] = True
                    except IndexError:  # key 'C_der_nor' does not yet exist in 'self.Tree'
                        self.Tree[C_der_nor].insert(0, True)
                    break
                for tree_index in index_list:
                    new_tree_index = list(tree_index)
                    new_tree_index.append(nu)
                    # new_index_list.append(new_tree_index)
                    if C_der_nor not in self.Tree.keys():
                        d_derived[C_der_nor].append(new_tree_index)
                        nothing_new = False
                    self.Tree[C_der_nor].append(new_tree_index)
        # 4. ##############################################################
        # (if an element turned out to be successful later in the loop)
        for C_der_nor in d_derived.keys():
            path_to_node = []
            if C_der_nor in MapTree.list_of_successful:
                index_list = d_derived[C_der_nor]
                # print index_list
                path_to_node = self.mark_path_to_node_successful(index_list)
                self.eliminate_side_branches(index_list, d_derived)
                del d_derived[C_der_nor]
            for C in path_to_node:
                if C in self.Tree.keys():
                    index_list = self.get_Tree_key(self.Tree[C])
                    self.eliminate_children(index_list, d_derived)

        self.d_derived = d_derived  # deletes the old one
        if nothing_new: print "nothing new"
        return

    def __str__(self):
        for C, index_list in self.d_derived.items():
            print p.array(C), " --> ", index_list, "\n"
        return ""

    def run(self):
        counter = 0
        # print self
        while any(MapTree.list_of_defects):
            counter += 1
            self.strategy_step()
            if counter == 6: break


# if  raw_input("ENTER to continue") == '':
#                    print "unsolved cases: ", len(MapTree.list_of_defects) - MapTree.list_of_defects.count(0)
#                    #print MapTree.list_of_successful
#                    counter = 0
#                    continue
#                else:
#                    print self
#                    break

def generate_list(**kwargs):
    T = MapTree(**kwargs)
    T.run()
    # To_File(T.Tree)
    # Output_as_Graph(Tree_to_TeX(T.Tree))
    # print "len(MapTree.list_of_successful): ",  len(MapTree.list_of_successful)
    # print(T)


    count = 0
    list_of_unsolved = []
    for C_init in MapTree.list_of_C_init:
        # if C_init not in MapTree.list_of_successful:
        # if C_init not in list_of_unsolved:
        count += 1
        C = p.array(C_init)
        # print count, ". \n", C, " defect: ".ljust(9), Q.Defect(C)
        list_of_unsolved.append(C)

    # this part prints the tree as a graph
    # from Tree_to_TikZ_Graph import *
    # inputfile = "tree_for_graph_r4"
    # with open(inputfile, "r") as file: Tree = pickle.load(file)
    ##print(Tree)
    # print(Output_as_Graph(Tree_to_TeX(Tree)))


    list_of_unsolved_array = [p.array(C_init) for C_init in list_of_unsolved]
    # as file with Python-list

    from utils import to_file
    outputfile = 'unsolved_after_TreeMap.pi'
    to_file(list_of_unsolved_array, outputfile)

    # as TeX-formatted output
    import TeX
    filename = 'unsolved_after_TreeMap.tex'
    TeX.to_file(TeX.Quasicones_to_TeX(list_of_unsolved_array), filename)
