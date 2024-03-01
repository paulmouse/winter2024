# 10, 50, 100, 200, 500, 1000, 2000, 5000
# import itertools
#
#
# def sumFromListCombination():
#     lst = [10, 50, 100, 200, 500, 1000, 2000, 5000]
#     # lstlen = len(lst)
#     sumlst = []
#     allSums = itertools.chain((itertools.combinations(lst, r)) for r in range(len(lst)+1))
#     # print(*allSums)
#     for i in allSums:
#         print(*i, end='\n')
#
#     #     sumlst.append(i)
#     # print(*sumlst)
#
#         # if lstlen <= len(lst):
#         #     sumFromListCombination(lstlen)
#         #     lstlen += 1
#         # else:
#         #     break
#
# sumFromListCombination()


import itertools

banknotes = [10, 50, 100, 200, 500, 1000, 2000, 5000]
sums = []

for j in range(1, len(banknotes) + 1):
    #    for i in itertools.combinations([1,2,3,4,5], j):
    for i in itertools.combinations(banknotes, j):
        #print(i, '|', sum(i))
        x = sums.append(sum(i))
        #print(x)

sums_uniq = set(sums)
print(sorted(sums_uniq))

