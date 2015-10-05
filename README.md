# Strategies for support quasicones of affine Lie algebras of type A

## modules of the package Quasicone and dependencies

'''
Quasicone.Iterator()

Quasicone.Weyl_normal( pylab.array )

Quasicone.Strategy_iterator( list, itertools)

Quasicone.parameters # n = 3

Quasicone.Apply_strategy
'''

**Steps**

1. Compute the Quasicones below the bound, characterized by 'parameters.max'. The array being returned are iterator instances.
2. Apply strategies to each of the quasicones and return the Weyl normal form of the result.
3. The non-solved quasicones are saved in a file (pickled), list_of_exceptionals_r[rank]
4. The more advance algorithm TreeMap is applied to these non-solved quasicones.
5. Quasicones still not solved are returned in form of a file (pickled) called 'list_of_extraexceptionals'.
6. The left-over cases can be solved by try and error with the help of 'Interactive_RootSteps.py' and your own intuition.

- The pickled list of yet unsolved quasicones is printed in shape of a human readable TeX-file. Declare the output file or use the pattern from the run.sh script
- also the stepwise solution is represented, when opting-in the TeX-output in the files list_of_*.py
- For the MapTree-algorithm an illustration of the search tree can be produced, by means of the 'Tree_to_TikZ_Graph.py' script
