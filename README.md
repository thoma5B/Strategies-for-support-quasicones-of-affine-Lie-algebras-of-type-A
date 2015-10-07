# Strategies for support quasicones of affine Lie algebras of type A

## how it works

A full description of the theory behind this can be found at my thesis at http://arxiv.org/...

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

## Complexity

Implementation is still only single threaded, thus multicore-processor can not provide performance boost, yet. Theoretical consideration on the complexity of the proplem is treated in Chapter 5 of the thesis.

### Example

if only run 'list_of_exceptionals'
- with r = 3 and max = 3, then execution time (on 2.4 GHz machine) < 40 sec
- with r = 4 and max = 4, then execution time (on 2.4 GHz machine) > 1:03 hs

if only run 'Concatenate_Strategies'
- with r = 4 and max = 4, then
execution time (on 2.4 GHz machine) > 4 hs


## Modules of the package Quasicone and dependencies

```
Quasicone( json )
Quasicone.Iterator( collections )
Quasicone.Weyl_normal( numpy.array )
Quasicone.Strategy( itertools )
Quasicone.Apply_strategy( numpy, collections, json )
Concatenate_Strategies( numpy, collections, json, pickle, Quasicone )
list_of_exceptionals( copy, numpy, math, pickle )
Tree_to_TikZ_Graph( latex-packages: tikz, tkz-berge, fp )

parameters.json
```
