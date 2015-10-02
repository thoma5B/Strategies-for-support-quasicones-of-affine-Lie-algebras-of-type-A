import math as m
from numpy import *
#import copy as c
from collections import deque, defaultdict


def rootsum(i, j):
    return sum((2**k) for k in range(i, j))


def Index_to_Root(i, j):
    if i<j: x = rootsum(i, j)
    elif i>j: x = -rootsum(j, i)
    else: x = 0
    return x


def Root_to_Index( x):
    if x == 0: return [0, 0]
    y = abs(x)
    i = 0
    while y & 1 == 0:
        y >>= 1
        i += 1
    j = i
    while y & 1 == 1:
        y >>= 1
        j += 1
    if (y != 0 or i >= n) or j >= n: return [0, 0]
    if x > 0: return [i, j]
    else: return [j, i]
