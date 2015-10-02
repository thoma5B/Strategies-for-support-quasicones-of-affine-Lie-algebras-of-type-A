import math as m
import pylab as p
import copy as c

def Associate_Index(i, j):
    if i<j: x = sum((2**k) for k in range(i, j))
    elif i>j: x = -sum((2**k) for k in range(j, i))
    else: x = 0
    return x


#def Create_Indices():  # this is the integer denomination of the roots
#    IndexMatrix = zeroes(n)
#    for i in xrange (0, n):
#        for j in xrange (0, n):
#            IndexMatrix[i][j] = Associate_Index(i, j)
#    return IndexMatrix


def Iterate_Nondiag():     # a fast iteration through all off-diag. matrix elements
    for ii in xrange(0, n):
        for jj in xrange(0, n):
            if ii == jj: continue
            yield [ii, jj]
            

def Next( i, j):     # next element in the lower triangle 
    offdiag = j - i
    if [i, j] == [n - 1, 0]: return [0, 0]
    if offdiag < 0:
        if offdiag > - n + 1:
            if i < n - 1: i += 1; j += 1; 
            else: 
                offdiag -= 1 
                i =- offdiag 
                j = 0 
        else: print"exception in 'Next(i, j)'"
    return [i, j]


def Previous( i, j):
    offdiag = j - i
    if [i, j] == [1, 0]: return [0, 0]
    if offdiag < 0:
        if offdiag > -n:
            if j > 0: i -= 1; j -= 1
            else: offdiag += 1; i = n - 1; j = i + offdiag
        else: print"0,0"; [i, j] = [0, 0]
    return [i, j]

    
def Iterate_subdiag( i = 1, j = 0):  
    while True:
        yield [i, j]
        [i, j] = Next(i, j)
        if [i, j] == [0, 0]: break
        

def Iterate_reverse_subdiag( i, j):
    while True:
        [i, j] = Previous(i, j)
        yield [i, j]
        if [i, j] == [1, 0]: break


def zeroes(n):
    C = []
    for i in range (0, n):
        D = [] 
        for j in range (0, n):
            D.append(0)
        C.append(D)
    return p.array(C)


def normal():
    C = zeroes(n)
    for i in range (1, n):
        C[i-1][i] = 1 
    return C


def start_matrix():
    C = normal()
    for ii in xrange (0, n):
        for offdiag in range(1, n-ii):
            C[ii][ii + offdiag] = offdiag #above upper diagonal
            C[ii + offdiag][ii] = -offdiag # +2
    C[1, 0] = 2
    return C
    
    
def gap_start_matrix(): # puts '2' in every field in the subdiagonal triangle
    C = zeroes(n)
    C[1, 0] = 3
    return C


def IndexinMatrix( x):
    if x == 0: return [0, 0]
    y = abs(x)
    i = 0 
    while y & 1 == 0:
        y = y >> 1
        i += 1
    j = i
    while y & 1 == 1:
        y = y >> 1
        j += 1
    if (y != 0 or i >= n) or j >= n: return [0, 0]
    if x > 0: return [i, j]
    else: return [j, i]



def Defect(C):
    defect = 0
    for [i, j] in Iterate_subdiag(1, 0): # iterate through all subdiag el.
        gap = C[i, j] + C[j, i]
        if gap > 2: defect += gap - 2
        elif gap < 0:       # only a subalgebra A_n'^(1) acts non-trivially
            #print"gap < 0"; 
            return -1 
    return defect
 

def Weyl_normal_form(C):
    
    C_normal = C.copy()

    #reordering:
    auxiliary_array = []
    for [i, j] in Iterate_subdiag(1, 0):
        auxiliary_array.append([[i, j], C[i, j] + C[j, i]])
    sorted_array = sorted(auxiliary_array, key=lambda x: x[1], reverse=True)
    while sorted_array:
        [ii, jj] = sorted_array.pop(0)[0]
        [i, j] = auxiliary_array.pop(0)[0]
        C_normal[i, j] = C[ii, jj]
        C_normal[j, i] = C[jj, ii]

    #shifting:
    shift_vec = []
    for [i, j] in Iterate_subdiag(1, 0):
        if i - j == 1: 
            if C_normal[j, i] == 1: shift_vec.append(0)
            else:
                shift_ji = 1 - C_normal[j, i]
                shift_vec.append(shift_ji)
                C_normal[j, i] = 1
                C_normal[i, j] -= shift_ji
        else:
            C_normal[j, i] += sum(shift_vec[j:i] )
            C_normal[i, j] -= sum(shift_vec[j:i] )
    return C_normal


data_string = ""

def Output():
    
    output_string = "\documentclass[10pt,a4paper]{elsarticle} \n"
    output_string += "\\usepackage{amsmath} \n"
    output_string += "\\usepackage{amssymb} \n"
    output_string += "\\usepackage[hmargin=0.5cm, vmargin=0.5cm]{geometry} \n"
    output_string += "\\begin{document} \n \\scriptsize"
    output_string += " all quasi-cones on start w.r.t. "\
                + "$V_{\lambda-\delta}$, whereas $V_{\\lambda}=\\left\\{0\\right\\}$ \n\n"
    output_string += data_string
    output_string += "\n total number of considered quasicones: "\
                    + str(Apply_strategy._counter)
#        output_string += "\n number of cones:" + str(self._admissible_count)
    output_string += "\n \\end{document}"
    return output_string

class Apply_strategy():

    _counter = 0
    _critical_counter = 0
    list_of_exceptionals = []
    
    #from sets import Set
    
    def __init__(self, startweight, quasicone, list_of_operators):
        # Quasicone_Iterator.__init__(self) 
        # inherits the init method (not); otherwise it runs 'Quasicone_Iterator.run()' 
        self._weight = p.array(startweight).copy()
        self.Lie_closure_iteration_counter = 0 
        self.C_derived  = quasicone.copy()
        self._C         = quasicone.copy()
        self.defect = 0  # of self.C_derived
        self.list_of_operators = list_of_operators
        self.output = ""
        #print(quasicone)
        Apply_strategy._counter += 1
        self.run()


    def Correct_inequalities(self, i, j): 
        # correct all ineq's that might turn wrong after decreasing C[i, j]
        nothing_to_correct = True
        
        # show in theory: the diagonal determines the distance \
        # of the row from the element to be changed
        # here only correct row, since we are going through all element in the next
        # Argument: q equations, 2q variables, ...
        for jj in range(0, n):   # correct row
            if jj == i or jj == j : continue
            if self.C_derived[i, jj] > self.C_derived[i, j] + self.C_derived[j, jj]: 
                self.C_derived[i, jj] = self.C_derived[i, j] + self.C_derived[j, jj]
                nothing_to_correct = False
        return nothing_to_correct
        


    def Lie_closure(self):  #corrects all inequalities where C[i, j] occurs
        Lie_closure_iteration_counter = 1 
        # not '0' because in 'Root_step' one iteration occured already
        while True:
            #print "LieCl"
            nothing_to_correct = True
            for [i, j] in Iterate_Nondiag():
                if not self.Correct_inequalities(i, j): nothing_to_correct = False
            if nothing_to_correct: return Defect(self.C_derived)
            if Defect(self.C_derived) < 0: return
            Lie_closure_iteration_counter += 1
            # self.Matrix_to_Latex_string() # debugging info
            if Lie_closure_iteration_counter > self.Lie_closure_iteration_counter :
                self.Lie_closure_iteration_counter = Lie_closure_iteration_counter


    def Root_step(self, root): # weight=[0, -1] =~ \mu - \delta
        weight = self._weight.copy()
        self._weight = p.add(weight, root)
        [i, j] = IndexinMatrix( root[0] )  #
        [iii, jjj] = IndexinMatrix( self._weight[0] ) 
        if not [iii, jjj] == [0, 0] : 
            self.C_derived[jjj, iii] = -self._weight[1]   # this comes from the hole
        
        #diag = j - i
        # show in theory: the diagonal determines the distance \
        # of the rows/columns from the element to be changed
        
        if self.C_derived[j, i] + root[1] < 1 and not [jjj, iii] == [j, i]: 
            self.C_derived[j, i] = 1 - root[1]
        
        for jj in range(0, n):   # correct row
            if jj == j or jj == i: continue
            # i + diag = j
            if self.C_derived[j, jj] + root[1] < self.C_derived[i, jj]: 
                self.C_derived[j, jj] = self.C_derived[i, jj] - root[1]
        
        for ii in range(0, n):      # correct column
            if ii == i or ii == j: continue
            # j - diag = i
            #print(self.C_derived[ii, i], root[1], self.C_derived[ii, j])
            if self.C_derived[ii, i] + root[1] < self.C_derived[ii, j]: 
                self.C_derived[ii, i] = self.C_derived[ii, j] - root[1]
        
        self.Lie_closure()   
        return


    
    def Balance_of_quasicones(self):
        return Defect(self._C) - Defect(self.C_derived)


    def run(self):   # list or array ????
        # list of operators = pair e_index + k\delta
        # call with self.Balance_of_quasicones([1,0],[-1,0])  
        # ( e_{-\alpha} \circ e_{+\alpha} )
        Transform_sequence = []
        Operator_sequence = []
        
        if Defect(self.C_derived) <= 0: 
            self.successful = True
            return 
        self.successful = False
        
        delta = -1 # actually . = self._weight[1].copy()
        strategy = c.copy(self.list_of_operators) #unnecessary assignment
        im_root = 0 # = root[1]  # first step
        while strategy:
            root = [strategy.pop(0), im_root]    #last step        
            self.Root_step(root) # the first operation will be the application of e_{+\alpha} 
            Transform_sequence.append(self.C_derived.copy())
            Operator_sequence.append(root)
            delta += im_root
            if Defect(self.C_derived) <= 0: 
                self.successful = True
                #return 
            # now adopt strategy according to the previous transforms
            if (not strategy): break
            [iii, jjj] = IndexinMatrix( strategy[0] )
            im_root = self.C_derived[iii, jjj] - 1

#if delta > 0 or Defect(C_derived) <= 0: return
# dont print if the entire Cartan acts trivially or the operation yields 
# a complete cone
# or reduction to lower-dimensional case (in Theorie genauer ausfuehren)
        
        self.defect = Defect(self.C_derived)
        balance = self.Balance_of_quasicones()
        if delta == -1 and balance > 0: 
            self.successful = True
        
        if delta == -1 and balance > 2*(n - 1) - 1: 
            self.successful = True
        
        return 


# end class Apply_strategy ###################################################
# ############################################################################

def Matrix_to_Latex_string(Matrix): #'self' bc of static variable
    local_string = " $\left(\\begin{array}{"
    for i in range (0, n ): 
        local_string += "c"
    local_string += "} \n"
    for i in range (0, n ):
        for j in range (0, n ):
            local_string += str(Matrix[i, j])
            if not j == n - 1: local_string += " & "
        if not i == n - 1: local_string += "\\\\ \n"
    local_string += "\n \end{array}\\right)$ \n"
    return local_string


def Transform_to_Latex_string(root):  
    local_string = " $\overset{e_{\\alpha_{" \
                                    + str(root[0]) + "} + (" \
                                    + str(root[1]) + ")\\cdot\\delta" 
    local_string += "}}{\\rightsquigarrow}$ "
    #print " ---> \n"
    return local_string




def Strategy_Iterator(strategy = [1, 2, 4, -7]):
    yield strategy
    [i, j] = IndexinMatrix(strategy[-1])
    [i, j] = Previous(i, j)
    while [i, j] != [0, 0]:
        strategy = [strategy[k] for k in range(3)]
        strategy.append(Associate_Index(i, j)) #only the 4th root step
        #if new_instance.C_derived[i, j] > 1:
        rest = sum(strgy for strgy in strategy)
        while rest:
            #print"480" (this not)
            [ii, jj] = IndexinMatrix(rest)
            if [ii, jj] == [0, 0]: #e.g. if strategy[-1]=[-2,0]
                strategy.append(-2**int(m.ceil(m.log(rest,2))))
                #strategy.append([Associate_Index(iii, jjj), 0])
            else:
                strategy.append(-rest)
            rest = sum(strgy for strgy in strategy)
        yield strategy
        #print(i, j)
        [i, j] = Previous(i, j)
    return
        
        
#n = input(" % calculate A_n^(1); insert n: ") + 1
n = 3 + 1  # A_2^(1)
#n = 4 + 1 # 5 hs computing (on 2.4 GHz Intel i3 machine - single threading)

max = 4
startweight = [0, -1]
#strategy_1 = [[1, 0], [-1, 0]]

#strategy_2 = [[1, 0], [2, 0], [-3, 0]] # no exceptional cases for n = 2 + 1
# this is just a blueprint for the strategy
# the im_root part will be changed in the algorithm

import pickle

file = open("list_of_extraexceptionals", "r")
list_of_extraexceptionals = pickle.load(file)
file.close()

def To_File(list, filename):
    file = open(filename, "rw+")
    pickle.dump(list, file)
    file.close()
    return

mu =0
#non_seccess_counter = 0
#list_of_extraexceptionals = []
list_of_minimal_normalized_results = []

for quasicone in list_of_extraexceptionals:
    mu += 1
    nu = 0    
    list_of_results = []
    for strg in Strategy_Iterator():
        nu += 1
        #data_string += "%s.%s." %(mu,nu) 
        new_instance = Apply_strategy(startweight, quasicone, strg)
        #data_string += new_instance.output
        list_of_results.append([[mu,nu], new_instance.defect, new_instance.C_derived.copy()])

    min_defect = n*n
    for C in list_of_results:
        if C[1] < min_defect:
            min_defect = C[1]
     
    for C in list_of_results:
        if C[1] == min_defect:
            #list_of_minimal_normalized_results.append(Weyl_normal_form(C[2]))
            list_of_minimal_normalized_results.append(C[2])
            data_string += "%s.%s." %(C[0][0],C[0][1])
            #data_string += Matrix_to_Latex_string(C[2])
            data_string += Matrix_to_Latex_string(Weyl_normal_form(C[2]))
            data_string += "defect: %s \n\n" %C[1]
        

print(Output())
#To_File(list_of_extraexceptionals, "extraexceptional_cases.txt")
#To_File(list_of_minimal_normalized_results, "list_of_minimal_normalized_results")


