 #!usr/bin/env python
"""
execute by typing, e.g.
>python test.py -r 3 -m 4
#running algorithm for n = 4 and max = 4
#time:  38.5
"""

import Quasicone
from optparse import OptionParser
import sys
import logging
logging.basicConfig(level=logging.DEBUG)
#_logger = logging.getLogger(__name__)

from utils import timer

parser = OptionParser()
parser.add_option("-r", "--rank", dest="rank")
parser.add_option("-i", "--input", dest="input")
parser.add_option("-o", "--output", dest="output")
parser.add_option("-m", "--max", dest="max_gap")
(options, args) = parser.parse_args()
try:
    r = int(options.rank)
except TypeError, err:
    raise parser.error('options are \n \
    "-r", "--rank", dest="rank"'
    )
try:
    max = int(options.max_gap)
except TypeError:
    print 'no max indicated, I\'ll take the default one (r+1)'

kwargs = {  'n' : r + 1,
            'max' : r + 1,
            "extraexceptionals": "extraexceptionals_r{}.pi".format(r),
            "exceptionals": "exceptionals_r{}.pi".format(r),
            "startweight": [0, -1] }

Quasicone.__init__(**kwargs)
print 'running algorithm for n =', kwargs['n'],\
        'and max =', kwargs['max']

@timer
def run():
    import list_of_exceptionals        # executes script 'list_of_exceptionals.py'
    #import list_of_extraexceptionals    # executes script 'list_of_extraexceptionals.py'
    #import Concatenate_Strategies       # executes script 'Concatenate_Strategies.py'
    return

run()
