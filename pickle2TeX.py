import pickle
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-i", "--input", dest="input")
parser.add_option("-o", "--output", dest="output")
(options, args) = parser.parse_args()

inputfile = options.input
outputfile = options.output

if inputfile:
    file = open(inputfile, "r")
    in_list_of_Quasicones = pickle.load(file)
    file.close()

import TeX

TeX.to_file(TeX.Quasicones_to_TeX(in_list_of_Quasicones), outputfile)
