import pickle
import Set
import pylab
import Quasicone
import TeX

from optparse import OptionParser 

parser = OptionParser()
parser.add_option("-r", "--rank", dest="rank")
parser.add_option("-i", "--input", dest="input")
parser.add_option("-o", "--output", dest="output")
(options, args) = parser.parse_args()
r = int(options.rank) 
inputfile = options.input
outputfile = options.output

n = r + 1  # could also get n through : n = len(in_list_of_Quasicones[0]._C)

if inputfile:
    file = open(inputfile, "r")
    in_list_of_Quasicones = pickle.load(file)
    file.close()
else: print"no inputfile indicated; use option -i [filename]"

print(TeX.Output(TeX.Quasicones_to_TeX(in_list_of_Quasicones)))
