#!/bin/sh

echo enter rank, "n = r + 1; A_r"
read rank

#################################
# exceptionals of rank r:
#################################
#
# python -O test.py -r $rank
#
# # example: Case r = 4, max = 4 : start: 16:55:49 end: 17:59:33 => time = 1:03:16 hs
#
# rm list_of_exceptionals_r$rank.pdf
# pdflatex list_of_exceptionals_r$rank.tex
#
#
# ######################################
# # list_of_extraexceptionals of rank r:
# ######################################
#
# python -O list_of_extraexceptionals.py \
# -r $rank \
#
# rm list_of_extraexceptionals_r$rank.pdf
# pdflatex list_of_extraexceptionals_r$rank.tex

# open pdf-viewer:
#evince /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.pdf


###################################
# unsolved_after_TreeMap of rank r:
###################################

python -O test.py -r $rank

rm unsolved_after_TreeMap_r$rank.pdf
pdflatex unsolved_after_TreeMap_r$rank.tex
# open pdf-viewer:
#evince unsolved_after_TreeMap.pdf
