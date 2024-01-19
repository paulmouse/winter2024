# lst = [1, 3, 5, 7, 8, 9]
# for k, v in enumerate(lst, 1):
#     print(k, v)

# lst = [1, 3, 5, 7, 8, 9]
# lst2 = lst
# lst2 = lst[:]   # так буден новый список
# lst2 = lst * 1  # так буден новый список
# print(lst, lst2)
# lst2[0] = 123
# print(lst, lst2)


# lst = [1,2,3,4,5]
# lst2 = []
# for i, j in enumerate(lst):
#     summa = 0
#     for k in range(i+1):
#         summa += lst[k]
#     lst2.append(summa)
# print(lst2)

# lst = [1,2,3,4,5]
# lst2 = []
# summa = 0
# for i in (lst):
#     lst2.append(sum(lst[0:i+1]))
# print(lst2)