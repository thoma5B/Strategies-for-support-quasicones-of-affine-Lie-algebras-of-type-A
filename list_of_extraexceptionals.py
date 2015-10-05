import math as m
import numpy as p
import copy as c
import Quasicone

from optparse import OptionParser
from Quasicone.Apply_strategy import Apply_strategy
import json, pickle

with open("parameters.json", "rw+") as f:
    parameters = json.load(f)
startweight = parameters['startweight']
inputfile = parameters['exceptionals']
outputfile = parameters['extraexceptionals']
n = parameters['n']

import pickle
if inputfile:
    file = open(inputfile, "r")
    list_of_exceptionals = pickle.load(file)
    file.close()
else: print "no inputfile indicated; use option -i [filename]"


non_success_counter = 0
list_of_extraexceptionals = []

for mu, C in enumerate(list_of_exceptionals):
    sublist = []
    for nu, strg in enumerate(Quasicone.Strategy.iterator(n)):
        #print C._C
        new_instance = Apply_strategy(startweight = startweight,
                                        quasicone = C._C,
                                        list_of_operators = strg)
        new_instance.enumerator += [mu,nu]
        if new_instance.successful: break
        sublist.append(new_instance)
    else:           #only if all of the strategies do not accomplish
        non_success_counter += 1
        #list_of_extraexceptionals.append(sublist)
        list_of_extraexceptionals = p.concatenate((list_of_extraexceptionals, sublist))

from utils import to_file
to_file(list_of_extraexceptionals, outputfile)

import TeX
print(TeX.Output(TeX.Quasicones_to_TeX(list_of_extraexceptionals)))
