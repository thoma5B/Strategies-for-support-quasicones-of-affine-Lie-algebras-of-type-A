import numpy as p

from Iterator import subdiag
import json

with open("parameters.json", "rw+") as f:
    parameters = json.load(f)
n = parameters['n']


def transposition_labeled_sort(L, key=lambda x: x, reverse=False):
    # sorting algorithm that remembers sign of transposition
    # a modification of 'selection sort'
    signs = p.ones(len(L))  # the transposition signs

    if reverse:
        eps = -1
    else:
        eps = 1

    for j in range(n):
        # find the min element in the unsorted a[j .. n-1]
        # assume the min is the first element
        iMin = j
        # test against elements after j to find the smallest
        for i in range(j + 1, n):
            # if this element is less, then it is the new minimum
            if eps * key(L[i]) < eps * key(L[iMin]):  # found new minimum
                iMin = i  # remember its index
        if iMin != j:
            L[j], L[iMin] = L[iMin], L[j]  # swap positions
            signs[j] *= -1
            signs[iMin] *= -1
    return L, list(signs)


def Weyl_normal_form(C):
    # C_normal = C.copy()
    auxiliary_array = []  # reordering:
    for [i, j] in iter(subdiag):
        auxiliary_array.append([[i, j], C[i, j] + C[j, i]])
    sorted_array, signs = transposition_labeled_sort(auxiliary_array, key=lambda x: x[1], reverse=True)
    while sorted_array:
        [ii, jj] = sorted_array.pop(0)[0]
        if signs.pop(0) == 1:
            [i, j] = auxiliary_array.pop(0)[0]
        else:
            [j, i] = auxiliary_array.pop(0)[0]
        # C_normal[i, j] = C[ii, jj]  #
        # C_normal[j, i] = C[jj, ii]
        C[i, :], C[ii, :] = C[ii, :], C[i, :]  # swap rows
        C[:, j], C[:, jj] = C[:, jj], C[:, j]  # then swap columns
    shift_vec = []  # shifting:
    for [i, j] in iter(subdiag):
        if i - j == 1:
            if C[j, i] == 1:
                shift_vec.append(0)
            else:
                shift_ji = 1 - C[j, i]
                shift_vec.append(shift_ji)
                C[j, i] = 1
                C[i, j] -= shift_ji
        else:
            C[j, i] += sum(shift_vec[j:i])
            C[i, j] -= sum(shift_vec[j:i])
    return C
