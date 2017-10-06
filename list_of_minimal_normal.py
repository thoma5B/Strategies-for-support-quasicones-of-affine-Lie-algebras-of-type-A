"""deprecated, since part of 'Concatenate_Strategies.py'"""

import numpy as p
import json

import Quasicone
from TeX import Matrix_to_Latex_string

with open("parameters.json", "rw+") as f:
    parameters = json.load(f)

n = parameters['n']

startweight = parameters['startweight']
inputfile = parameters['inputfile']
outputfile = parameters['outputfile']

import pickle

if inputfile:
    file = open(inputfile, "r")
    list_of_extraexceptionals = pickle.load(file)
    file.close()
else:
    print "no inputfile indicated; use option -i [filename]"

mu = 0
non_success_counter = 0
data_string = " "

list_of_results = []
list_of_lists = []
list_of_minimal_normal = []
if p.any(list_of_extraexceptionals):
    reference_cone = list_of_extraexceptionals[0]._C
else:
    data_string += " list_of_extraexceptionals empty"

for C in list_of_extraexceptionals:
    if p.any(C._C - reference_cone):  # C._C != reference_cone
        list_of_lists.append(list_of_results)
        list_of_results = []
    if C.successful or list_of_results == [True]:
        list_of_results = [True]
    else:
        list_of_results.append(C)
    # only if all of the strategies do not accomplish
    reference_cone = C._C.copy()
list_of_lists.append(list_of_results)

for list_of_results in list_of_lists:
    if list_of_results[0] == 0: continue
    min_defect = n * n
    for C in list_of_results:
        if C.defect < min_defect:
            min_defect = C.defect.copy()

    for C in list_of_results:
        if C.defect == min_defect:
            C_derived_normal = Quasicone.Weyl_normal_form(C.C_derived)
            list_of_minimal_normal.append(C_derived_normal)
            data_string += C.enumerator
            data_string += Matrix_to_Latex_string(C_derived_normal, n)
            data_string += "\\; defect: %s -- balance: %s \n\n" % (C.defect, C.balance)

import TeX

print(TeX.Output(data_string))
