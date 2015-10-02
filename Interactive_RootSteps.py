from collections import defaultdict
import numpy as p
import Quasicone2 as Q


n = 5
Q.n = n
#print "in Concat", Q.n
inputfile = "list_of_specialexceptionals_r4"
#outputfile = "tree_for_graph_r4"


# File Operations %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import pickle
try: 
    with open(inputfile, "r") as file:
        list_of_exceptionals = pickle.load(file)
except IOError, err: 
    print err, "-- probably no inputfile indicated; use option -i [filename]"

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


as_tuple = lambda C : tuple(tuple(C[i]) for i in range(n)) # for an nxn-array
startweight = [0, -1]
    
    
class map_tree():

    
    def __init__(self, list_of_exceptionals):
        mu = 0
        for C in list_of_exceptionals:
            C_init = as_tuple(C)
                
    
    def __str__(self):
        for C, index_list in self.d_derived.items():
            print p.array(C), " --> ", index_list, "\n"
        return ""


    def run(self):
        self.strategy_step()
        root = raw_input("enter root (dual exponential)")


T.run()

import TeX
print(TeX.Output(TeX.Quasicones_to_TeX(list_of_unsolved_array)))
