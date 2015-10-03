from collections import deque

from parameters import parameters
n = parameters['n']

Iterate_Nondiag = iter([(i,j) for i in range(n) for j in range(n) if i != j])
subdiag = [(j + offdiag, j) for offdiag in range(1, n) for j in range(n - offdiag)]
subdiag_indices_iter = lambda i, j : iter(subdiag(n)[subdiag(n).index((i, j)) : ])
reversed_subdiag_iter = lambda i, j : reversed(subdiag[:subdiag.index((i, j))])


def Iterator(n, max):

    Zeros = zeros((n,n),int) 						# from numpy import *

    def start_matrix():
        C = Zeros
        for ii in range (0, n):
            for offdiag in range(1, n - ii):
                C[ii, ii + offdiag] = offdiag 		# above upper diagonal
                C[ii + offdiag, ii] = -offdiag 		# +2
        C[1, 0] = 2
        return C

    Startmatrix = start_matrix()
    _C = Startmatrix.copy()
    _Gap = {}           							# create empty dictionary
    _Gap[(1, 0)] = 3    							# put one value


    def Check_inequalities(): 						# checks all inequalities
        for [i, j] in Iterate_Nondiag(n):
            for jj in range(0, n):   				# correct row
                if jj == i or jj == j : continue
                if _C[i, jj] > _C[i, j] + _C[j, jj]:
                    return False
        return True


    def Reset_Gaps( i, j):   						# (max,max,2,2,2) -> (3,3,3,2,2)
        if [i, j] == [1, 0]: return [1, 0]
        Gapij = _Gap.get((i, j), 0)  				# Gap entry at index [i, j]
        											# if available, 0 else
        for (ii, jj) in reversed_subdiag_iter(i, j):
            _Gap[(ii, jj)] = Gapij
        return [ii, jj]


    def Gaps_deque(i = 1, j = 0):  					# Iterate_Gaps
        gaplist = deque([])							# from collections : double ended queue

        while _Gap.get((n - 1, 0), 0) < max:
            if [i, j] == [1, 0]:   					# i == 1 and j == 0
                while _Gap[(1, 0)] < max:
                    _Gap[(1, 0)] += 1
                    gaplist.append( _Gap )
            it1, it2 = subdiag_indices_iter(i, j), subdiag_indices_iter(i, j)
            next(i2)
            for (i, j) in it1:      				# find root where gap ...
                if _Gap[next(it2, 0)] < _Gap[(i, j)]:
                    (i, j) = next(it1)				# ... can still be increased ...
                    break
            _Gap[(i, j)] += 1    					# ... and increase it
            [i, j] = Reset_Gaps(i, j)
            gaplist.append( _Gap )
        return gaplist


    def Reset_Pairs( Gap,  i, j):          			# below subdiagonal
        if [i, j] == [2, 0]: return [2, 0]
        for [i, j] in reversed_subdiag_iter(i, j):
            x = Startmatrix[j, i]
            _C[j, i] = x         			  		# in upper triangle
            _C[i, j] = Gap[i, j] - x
            if [i, j] == [2, 0]: return [2, 0]

    # #############################################################################
    # main function ###############################################################
    # #############################################################################

    for Gap in iter(Gaps_deque()):
        for i in xrange(0, n - 1):   				# start with [i,j]=[1,0]
            _C[i + 1, i] = Gap[i + 1, i] - 1 		# subdiagonal
        for [i, j] in subdiag_indices_iter(2, 0): 	# i>j+1, i.e. triangle below subdiagonal
            x = Startmatrix[j, i]
            _C[j, i], _C[i, j] = x, Gap[i, j] - x   # in upper diagonal
        while True:
            while _C[i, j] < _C[i - 1, j] + _C[i, i - 1]: # one of the inequalities
                _C[i, j] += 1
                _C[j, i] -= 1
                if Check_inequalities():
                    yield _C
                [i, j] = [2, 0]
            for [i, j] in subdiag_indices_iter(i, j):
                if _C[i, j] < _C[i - 1, j] + _C[i, i - 1]:
                    break
            else: break
            _C[i, j] += 1
            _C[j, i] -= 1
            [i, j] = Reset_Pairs(Gap, i, j)
            if Check_inequalities():
                yield _C
    return
