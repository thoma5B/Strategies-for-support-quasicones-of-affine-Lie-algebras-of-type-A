#!/bin/sh

echo enter Filname:
read vs
echo enter rank, "n = r + 1; A_r"
read rank


python -OO /home/thomas/Documents/Doctoral_Thesis/Python/$vs.py -r $rank > /home/thomas/Documents/Doctoral_Thesis/Python/$vs

python -OO /home/thomas/Documents/Doctoral_Thesis/Python/Read_File_Save_TeX.py -f $vs > /home/thomas/Documents/Doctoral_Thesis/Python/$vs.tex

pdflatex /home/thomas/Documents/Doctoral_Thesis/Python/$vs.tex /home/thomas/Documents/Doctoral_Thesis/Python/Output_Quasic$vs.pdf

evince /home/thomas/Documents/Doctoral_Thesis/Python/Output_Quasic$vs.pdf &

exit

#################################
# list_of_exceptionals of rank r:
#################################

#> /home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals_r$rank

#python -O /home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals.py \
#-r $rank \
#-o list_of_exceptionals_r$rank \
#> /home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals_r$rank.tex

# n=4 : start: 16:55:49 end: 17:59:33 => time = 1:03:16 hs

#pdflatex /home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals_r$rank.tex
#/home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals_r$rank.pdf

#evince /home/thomas/Documents/Doctoral_Thesis/Python/list_of_exceptionals_r$rank.pdf


######################################
# list_of_extraexceptionals of rank r:
######################################

> /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank

python -O /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals.py \
-r $rank \
-i list_of_exceptionals_r$rank \
-o list_of_extraexceptionals_r$rank \
> /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.tex

#rm -f /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.*
pdflatex /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.tex
#/home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.pdf

# open pdf-viewer:
#evince /home/thomas/Documents/Doctoral_Thesis/Python/list_of_extraexceptionals_r$rank.pdf


###################################
# list_of_minimal_normal of rank r:
###################################

python -O /home/thomas/Documents/Doctoral_Thesis/Python/list_of_minimal_normal.py \
-r $rank \
-i list_of_extraexceptionals_r$rank \
> /home/thomas/Documents/Doctoral_Thesis/Python/list_of_minimal_normal_r$rank.tex

pdflatex /home/thomas/Documents/Doctoral_Thesis/Python/list_of_minimal_normal_r$rank.tex

# open pdf-viewer:
#evince /home/thomas/Documents/Doctoral_Thesis/Python/list_of_minimal_normal_r$rank.pdf
