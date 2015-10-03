

import Quasicone
from optparse import OptionParser
import sys

parser = OptionParser()
parser.add_option("-r", "--rank", dest="rank")
parser.add_option("-i", "--input", dest="input")
parser.add_option("-o", "--output", dest="output")
(options, args) = parser.parse_args()
try:
    r = int(options.rank)
    inputfile = options.input
    outputfile = options.output
except TypeError, err:
    raise parser.error('options are \n \
    "-r", "--rank", dest="rank"\n \
    "-i", "--input", dest="input"\n \
    "-o", "--output", dest="output")'
    )

kwargs = { 'n' : r + 1, 'max' : 4, 'startweight' : [0, -1]}

Quasicone.__init__(**kwargs)
print Quasicone.parameters['n']
print Quasicone.Iterator.subdiag
