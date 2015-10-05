"""
computes the image of applying the initial strategy to each of
all quasicones
:input: iterator through quasicones
:output: the non-solved quasicones as pickle in the file 'default_outputfile.pi'
and as TeX in the file 'quasicones_rank[n].tex'
"""

import math as m
import pylab as p
import copy as c
import Quasicone
from Quasicone.Apply_strategy import Apply_strategy
import json

with open("parameters.json", "rw+") as f:
    parameters = json.load(f)

startweight = parameters['startweight']
outputfile = parameters['exceptionals']

list_of_exceptionals = []
initial_strategy = Quasicone.Strategy.initial()

for mu, quasicone in enumerate(Quasicone.Iterator.iterator()):
    # print 'list_of_exceptionals line 24', mu, '\n', quasicone
    new_instance = \
        Apply_strategy(quasicone, initial_strategy)
    #print 'new_instance', new_instance
    new_instance.enumerator.append(mu)
    if new_instance.successful: pass # do nothing
    else: list_of_exceptionals.append(new_instance)

from utils import to_file
to_file(list_of_exceptionals, outputfile)

import TeX
filename = 'quasicones_rank{}.tex'.format( str(Quasicone.Iterator.n - 1) )
TeX.to_file(TeX.Quasicones_to_TeX(list_of_exceptionals), filename)
