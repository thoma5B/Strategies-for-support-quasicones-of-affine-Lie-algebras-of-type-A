import math as m
import pylab as p
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

#if inputfile:
#    file = open(inputfile, "r")
#    list_of_exceptionals = pickle.load(file)
#    file.close()
#

def To_File(list):
    if outputfile:
        file = open(outputfile, "w")
        pickle.dump(list, file)
        file.close()
    else: print"no outputfile indicated; use option -o [filename]"
    return


list_of_exceptionals = []
initial_strategy = Quasicone.Initial_Strategy()

for mu, quasicone in enumerate(Quasicone.Iterator()):
    new_instance = \
        Quasicone.Apply_strategy(startweight, quasicone, initial_strategy)
    new_instance.enumerator.append(mu) 
    if new_instance.successful: pass # do nothing
    else: list_of_exceptionals.append(new_instance)


To_File(list_of_exceptionals)


import TeX
print(TeX.Output(TeX.Quasicones_to_TeX(list_of_exceptionals)))
