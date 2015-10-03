import numpy as p

from Iterator import subdiag
from parameters import parameters
n = parameters['n']

def transposition_labeled_sort(L, key = lambda x: x, reverse=False):
	# sorting algorithm that remembers sign of transposition
	# a modification of 'selection sort'
	sign = p.ones(length(L))

	if reverse == False : eps = 1					# the transposition sign
	else: eps = -1

	for j in range(n-1):
    	# find the min element in the unsorted a[j .. n-1]
    	# assume the min is the first element
		iMin = j
    	# test against elements after j to find the smallest
		for i in range(j+1, i):
		    # if this element is less, then it is the new minimum
		    if eps*key(L[i]) < eps*key(L[iMin]): 	# found new minimum
		        iMin = i 							# remember its index
		if iMin != j:
		    L[j], L[iMin] = L[iMin], L[j] # swap positions
		    sign[j]    *= -1
		    sign[iMin] *= -1
	return dict(zip(L,sign))


def Weyl_normal_form(C):

    C_normal = C.copy()
    auxiliary_array = []                        	# reordering:
    for [i, j] in iter(subdiag):
        auxiliary_array.append([[i, j], C[i, j] + C[j, i]])
    sorted_dict = transposition_labeled_sort(auxiliary_array, key = lambda x: x[1], reverse=True)
    while sorted_dict:
        element = sorted_dict.pop(0)[0]
        [ii, jj] = element.key()
        if element.value() == 1:
        	[i, j] = auxiliary_array.pop(0)[0]
        else:
        	[j, i] = auxiliary_array.pop(0)[0]
        C_normal[i, j] = C[ii, jj]
        C_normal[j, i] = C[jj, ii]
    shift_vec = []                              	# shifting:
    for [i, j] in iter(subdiag):
        if i - j == 1:
            if C_normal[j, i] == 1: shift_vec.append(0)
            else:
                shift_ji = 1 - C_normal[j, i]
                shift_vec.append(shift_ji)
                C_normal[j, i] = 1
                C_normal[i, j] -= shift_ji
        else:
            C_normal[j, i] += sum(shift_vec[j:i] )
            C_normal[i, j] -= sum(shift_vec[j:i] )
    return C_normal
