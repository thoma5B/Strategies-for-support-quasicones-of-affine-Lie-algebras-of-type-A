
from collections import deque
from numpy import array, add
from Iterator import *
from utils import  Root_to_Index
import json

#retrieve global parameter 'n'
with open("parameters.json", "rw+") as f:
    parameters = json.load(f)
n = parameters['n']


def Defect(C):
    defect = 0
    for [i, j] in subdiag: 					# iterate through all subdiag el.
        gap = C[i, j] + C[j, i]
        if gap > 2: defect += gap - 2
        elif gap < 0:       						# only a subalgebra A_n'^(1) acts
        											# non-trivially
            return 0
    return defect


class Apply_strategy():

    def __init__(self, quasicone, list_of_operators, startweight):
        self._weight = array(startweight).copy()
        self.successful = False
        self.delta = -1 # actually . = self._weight[1].copy()
        self.Lie_closure_it_counter = 0
        self.C_derived  = array(quasicone)
        self._C         = array(quasicone)
        self.defect = Defect(self.C_derived)
        self.list_of_operators = list_of_operators
        self.Transform_sequence = []
        self.Operator_sequence = []
        self.enumerator = []
        self.run()


    def Correct_inequalities(self, i, j):
        # correct all ineq's that might turn wrong after decreasing C[i, j]
        nothing_to_correct = True
        # here, only correct row, since we are going through all element in the next
        # Argument: q = n.(n - 1) variables, q.(n - 2) equations
        for jj in range(0, n):   					# correct row
            if jj == i or jj == j : continue
            if self.C_derived[i, jj] > self.C_derived[i, j] + self.C_derived[j, jj]:
                self.C_derived[i, jj] = self.C_derived[i, j] + self.C_derived[j, jj]
                nothing_to_correct = False
        return nothing_to_correct


    def Lie_closure(self):
    	#corrects all inequalities where C[i, j] occurs
        Lie_closure_it_counter = 1
        # not '0' because in 'Root_step' one iteration occured already
        while True:
            nothing_to_correct = True
            for [i, j] in Iterate_Nondiag:
                if not self.Correct_inequalities(i, j): nothing_to_correct = False
            if nothing_to_correct: return Defect(self.C_derived)
            if Defect(self.C_derived) < 0: return
            Lie_closure_it_counter += 1
            if Lie_closure_it_counter > self.Lie_closure_it_counter :
                self.Lie_closure_it_counter = Lie_closure_it_counter


    def Root_step(self, root):      				# weight=[0, -1] =~ \mu - \delta
        weight = self._weight.copy()
        self._weight = add(weight, root)
        [i, j] = Root_to_Index( root[0], n )  #
        [iii, jjj] = Root_to_Index( self._weight[0], n )
        if not [iii, jjj] == [0, 0] :
            self.C_derived[jjj, iii] = -self._weight[1]   # this comes from the hole
        if self.C_derived[j, i] + root[1] < 1 and not [jjj, iii] == [j, i]:
            self.C_derived[j, i] = 1 - root[1]
        for jj in range(0, n):   # correct row
            if jj == j or jj == i: continue
            if self.C_derived[j, jj] + root[1] < self.C_derived[i, jj]:
                self.C_derived[j, jj] = self.C_derived[i, jj] - root[1]
        for ii in range(0, n):      # correct column
            if ii == i or ii == j: continue
            if self.C_derived[ii, i] + root[1] < self.C_derived[ii, j]:
                self.C_derived[ii, i] = self.C_derived[ii, j] - root[1]
        self.Lie_closure()
        return


    def Balance_of_quasicones(self):
        return Defect(self._C) - Defect(self.C_derived)


    def run(self):
        if self.defect <= 0:
            self.successful = True
            return
        strategy = deque(self.list_of_operators) 	#copy list
        im_root = 0
        while strategy:
            root = [strategy.popleft(), im_root]
            self.Root_step(root)
            # the first operation will be the application of e_{+\alpha}
            C_derived = self.C_derived.copy()
            self.Transform_sequence.append(C_derived)
            self.Operator_sequence.append(root)
            self.delta += im_root
            self.defect = Defect(C_derived)
            if self.defect <= 0:
                self.successful = True
            # now adopt strategy according to the previous transforms
            if (not strategy): break
            [iii, jjj] = Root_to_Index( strategy[0], n )
            im_root = self.C_derived[iii, jjj] - 1
        if self.delta > 0 or self.defect <= 0:
            self.successful = True
            return
        # dont print if the entire Cartan acts trivially or the operation yields
        # a complete cone
        # or reduction to lower-dimensional case
        self.balance = self.Balance_of_quasicones()
        if self.delta == -1 and self.balance > 0:
            self.successful = True
        # dont print if defect reduced and induction arg. applies
        if self.delta == -1 and self.balance > 2*(n - 1) - 1:
            self.successful = True
        # another case where induction arg. applies with a simple argument (Lemma 21)
        return
