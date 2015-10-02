
from itertools import combinations, chain

from parameters import n

def Initial_Strategy(n):							#e.g. [1, 2, 4, -7]
    initial_strategy = [2**i for i in range(n - 1)]
    initial_strategy.append(-rootsum(0, n - 1))
    return initial_strategy


def next_lower_root( x):
    if x :
        y = abs(x)
        pow2X = pow(2, n - 1)
        while y & pow2X == 0:
            pow2X >>= 1
        root = pow2X
        while True:
            pow2X >>= 1
            if y & pow2X: root |= pow2X
            else: break
        if x > 0: return root
        else: return -root
    else: return 0


def sum_to_n(n):
    "Generate the series of pos. integer lists which sum to a pos. integer, n"
    "by Thomas Guest http://wordaligned.org/articles/partitioning-with-python"
    from operator import sub
    b, mid, e = [0], list(range(1, n)), [n]
    splits = (d for i in range(n) for d in combinations(mid, i))
    return (list(map(sub, chain(s, e), chain(b, s))) for s in splits)


def Partition_of_Operators(n):
    for partition in sum_to_n(n - 1):
        ret_list = []
        start = 0
        for index in partition:
            ret_list.append(sum(2**i for i in range(start, start + index)))
            start += index
        yield ret_list


def Iterator(n): 							# with this, 'strategy' is a deque
    if n == 2:
        yield [1, -1]
        return
    for x in Strategy_Iterator(n - 1):
        yield x
    initial_strategy = Initial_Strategy(n)[:(n - 1)]
    for rest in Partition_of_Operators(n):
        strategy = list(initial_strategy)
        for x in rest: strategy.append(-x)
        yield strategy
        if len(rest) == 1: continue
        strategy = list(initial_strategy)
        for x in reversed(rest): strategy.append(-x)
        yield strategy
    return
