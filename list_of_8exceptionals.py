import math as m
import numpy as p
import copy as c
import Quasicone
# from parameters import parameters
# n=parameters['n']

import pickle

file = open("list_of_specialexceptionals_r4", "r")
list_of_specialexceptionals_r4 = pickle.load(file)
file.close()

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

import TeX
print(TeX.Output(TeX.Quasicones_to_TeX(list_of_extraexceptionals)))
