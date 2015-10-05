

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
except TypeError, err:
    raise parser.error('options are \n \
    "-r", "--rank", dest="rank"'
    )

kwargs = {  'n' : r + 1,
            'max' : 3 }

Quasicone.__init__(**kwargs)
print 'running algorithm for n =', kwargs['n'],\
        'and max =', kwargs['max']
import list_of_exceptionals # executes script 'list_of_exceptionals.py'
