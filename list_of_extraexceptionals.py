import math as m
import numpy as p
import copy as c
import Quasicone

from optparse import OptionParser 

parser = OptionParser()
parser.add_option("-r", "--rank", dest="rank")
parser.add_option("-i", "--input", dest="input")
parser.add_option("-o", "--output", dest="output")
(options, args) = parser.parse_args()
r = int(options.rank) 
inputfile = options.input
outputfile = options.output

n = r + 1
max = 4

Quasicone.n = n # touches the module's global variable
Quasicone.max = max
startweight = [0, -1]

import pickle

if inputfile:
    file = open(inputfile, "r")
    list_of_exceptionals = pickle.load(file)
    file.close()
else: print"no inputfile indicated; use option -i [filename]"

#file = open("list_of_exceptionals_r4", "r")
#list_of_exceptionals = pickle.load(file)
#file.close()

def To_File(list):
    if outputfile:
        file = open(outputfile, "w")
        pickle.dump(list, file)
        file.close()
    else: print"no outputfile indicated; use option -o [filename]"
    return


non_success_counter = 0
list_of_extraexceptionals = []

for mu, C in enumerate(list_of_exceptionals):
    sublist = []
    for nu, strg in enumerate(Quasicone.Strategy_Iterator()):
        new_instance = Quasicone.Apply_strategy(startweight, C._C, strg)
        new_instance.enumerator [mu,nu] 
        if new_instance.successful: break
        sublist.append(new_instance)
    else:           #only if all of the strategies do not accomplish
        non_success_counter += 1
        #list_of_extraexceptionals.append(sublist)
        list_of_extraexceptionals = p.concatenate((list_of_extraexceptionals, sublist))

To_File(list_of_extraexceptionals)

import TeX
print(TeX.Output(TeX.Quasicones_to_TeX(list_of_extraexceptionals)))
