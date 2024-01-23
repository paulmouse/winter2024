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

# lst = [[1,2,3], [10,20], [100, 200]]
# total = 0
# for subLst in lst:
#     print(subLst)
#     for i in subLst:
#         total += i
# print(total)


# lst = [[1,2,3], [10,20], [100, 200]]
# res = []
# total = 0
# for subLst in lst:
#     res += subLst
#     for i in res:
#         total = sum(res[0:i+1])
# print(res)
# print(total)

# a = 'Hello world'
# for i in range(len(a)):
#     print(i, a[i])
# # print(len(a))

# string1 = 'abccba'
# string2 = string1[::-1]
# if string1 == string2:
#     print('True')
# else:
#     print('False')

# string1 = 'abccba'
# for i in range(len(string1)):
#     if string1[i] != string1[-1-i]:
#         print(False)
#         break
# else: True

# lst = [1,5,7,89,99]
#
# print(lst.join('2'))


# alphabet = [chr(a) for a in range(97, 123)]
# lst = []
# for i in range(len(alphabet)):
#     lst.append(alphabet[i] * (i+1))
# print(lst)

# x = 5
#
# while x < 10:
#     print (x)
#     x+= 1
# else:
#     print('Else')

summa = 0
while True:
    x = int(input())
    if x < 0:
        break
    summa += x
print(summa)





