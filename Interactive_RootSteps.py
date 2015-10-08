"""
This program was designed to solve the remaining A_4^(1)-quasicones by Hand.

**currently not properly maintained and tested**

-performs root steps (transformations on the support of the module) in interaction
with the user. Root operators must be provided in shape of positive integers
that represent dual exponential of the simple part of the real root (modulo delta),
whose modulus is then computed by the programm.

-code was tested and the best way to it might be employed is inside an
'ipython notebook' which I did
"""

from collections import defaultdict
import numpy as p
import Quasicone.Apply_strategy as Q
import json

with open("parameters.json", "rw+") as f:
    parameters = json.load(f)

startweight = parameters['startweight']
n = parameters['n']

inputfile = "unsolved_after_TreeMap_r" + n - 1


# File Operations %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
import pickle
try:
    with open(inputfile, "r") as file:
        list_of_exceptionals = pickle.load(file)
except IOError, err:
    print err, "-- probably no inputfile indicated; use option -i [filename]"

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def generate_list():
    for i, C in enumerate(list_of_specialexceptionals_r4):
        while True:
            strg = input(" list of roots (dual exponential): ")
            if strg  == 0: break
            new_instance = Q.Apply_strategy([0, -1], C, strg)
            print i, ". \n", C, "\n ---", strg ,"--> \n", new_instance.C_derived, "\n defect =", new_instance.defect
            #if new_instance.defect <= 0 :
            #    print "next quasicone: \n"
            #    break

strg_list = [[-1,3],[1,-3],[1,2,-7,-2],[1,2,-7,-2],[-1,3],[1,-3],[1,2, -7, 12,7,-1,-8,-2,-6,3,6],[1,2, -7, -2,7,-3,-12,2,-3]]

def generate_TeX( strg_list = strg_list):
    import TeX
    for i, C in enumerate(list_of_specialexceptionals_r4):
        strg = strg_list[i]
        new_instance = Q.Apply_strategy([0, -1], C, strg)
        print TeX.Matrix_to_Latex_string(C, n = 5)
        print "\n \overset{"
        for root in reversed(strg) : print "e_{", root, "}\\circ"
        print "}{\\rightsquigarrow} \n",
            TeX.Matrix_to_Latex_string(new_instance.C_derived, n = 5)
