# 10, 50, 100, 200, 500, 1000, 2000, 5000
import itertools


def sumFromListCombination():
    lst = [10, 50, 100, 200, 500, 1000, 2000, 5000]
    # lstlen = len(lst)
    allSums = itertools.chain(itertools.combinations(lst, r) for r in range(1, len(lst) + 1))
    sumsSet = set()
    # for s in allSums:
    #     sumsSet.add(sum(s))
    return sorted(allSums)
        # if lstlen <= len(lst):
        #     sumFromListCombination(lstlen)
        #     lstlen += 1
        # else:
        #     break

sumFromListCombination()
