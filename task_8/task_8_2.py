# Задача 8-2
# На вход подается список, состоящий из списков чисел, например:
# [[1,5,3], [2,44,1, 4],[3,3]]
# Отсортируйте этот список по возрастанию общего количества цифр в каждом списочке.
# Каждый списочек отсортируйте по убыванию.


listOfList = [[1, 5444, 3], [2, 44, 1, 4], [3, 3]]
#subList = listOfList.reverse()
#print(subList)
# print(sum(len(str('1, 5444, 3'))))

def count(lst):                             # считаем количество цифр в подсписках не позиций, а ЦИФР
    #print(sum(len(str(x)) for x in lst))
    return sum(len(str(x)) for x in lst)

for sublist in listOfList:
    #print(sublist.sort(reverse=True))
    sublist.sort(reverse=True)

listOfList.sort(key=count)  # тут просто сортируем. тем самым присваиваем переменной новое значение


# и итог
print(listOfList)


# lst = [[1,5,3], [2,44,1, 4], [3,3]]
# def digits(lst):
#     res = 0
#     for i in lst:
#         res += len(str(i))
#     return res
# new_lst = sorted(lst, key = digits)
# print(new_lst)
# res = []
# for i in new_lst:
#     res.append(sorted(i, reverse = True))
# print(res)

