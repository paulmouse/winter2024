# s = 'abracadabra'
# for k in s:
#     print(k, s.find(k)) # ищем вхождение в строку. и нумеруем позицию
# a - 0
# b - 1
# r - 2
# a - 0
# ...

# hm = {}
# s = input()
# for k in s:
#     if k not in hm: # если ключа нет в словаре, принудительно вводим 0
#         hm[k] = 0
#     hm[k] = hm[k]+1 # ну а иначе увеличиваем на 1 индекс
# for k in hm:
#     print(k, hm[k])

# s = input()
# dct = {}
# for k in s:
#         if k not in dct:
#             dct[k] = 0
#         dct[k] += 1
# for k in dct:
#     print(k, dct[k])

# person ={
#     'name':'Mary',
#     'login': 'mmm',
#     'age' : 24
# }
# print(person)
# person['name'] = 'Ivan'
# print(person)

# dct2 = {
#     1:'mango',
#     2: 'orange',
#     3: 'apple'
# }
# print(dct2)
# sku = input()
# dct = {}
# count = 0
#
# while True:
#     if sku == 0: break
#     if sku in dct:
#         dct[sku] = dct[sku] + 1
#     else:
#         dct[sku] = 1
# print(dct)

# dct1 = {
#     True: 123,
#     False: 321
# }
# dct2 = {
#     False: 321,
#     True: 123
# }
# print(dct1 == dct2)

# dct1 = {
#     None: 123,
#     None: 321
# }
# print(dct1)

# dct = {'1':'один', '2':'два', '3':'три',
#        'один':'1','два': '2'}
#
# for i in input():
#     if i in dct:
#         print(dct[i], end=' ')
#     else:
#         print('*', end=' ')

# dct1 = {'a': 'qwe', 'b':'ewq'}
#
# dct2 ={}
# dct2['a'] = 'qwe'
# dct2['b'] = 'ewq'
#
# dct3 = dict(a = 'qwe', b = 'ewq')
#
# letter = ['a', 'b']
# letter2 = ['qwe', 'ewq']
# dct4 = dict(zip(letter, letter2))
#
#
#
# print(dct1, dct2, dct3, dct4)

# month = {1: 31,
#         2: 28,
#         3: 31,
#         4: 30,
#         5: 31,
#         6: 30,
#         7: 31,
#         8: 31,
#         9: 30,
#         10: 31,
#         11: 30,
#         12: 31
# }
# while True:
#     y = int(input())
#     m = int(input())
#     if y + m == 0:
#         break
#     if y % 4 == 0 and m == 2:
#         print(29)
#     else:
#         print(month[m])

# dct = {1:11, 2:22}
# print(dct)
# print(len(dct))


#частотный анализ
# str = 'На вход подаётся предложение слово буква поливинилхлорид'.split()
# dct ={}
# for words in str:
#     if words not in dct:
#         dct[words] = 0
#     dct[words] += 1
# print(dct)
#частотный анализ


# str = 'На вход На На подаётся предложение слово буква поливинилхлорид'.split()
# dct = {}
#
# for words in str:
#     if words not in dct:
#         dct[words] = 0
#     dct[words] += 1
# print(dct)
#
# word = str[0]
# for k in dct:
#     if dct[k] < dct[word]: # сменить знак для смены большее меньшее. обавление = изменит направление поиска
#         word = k
# print(word, dct[word])


#верность ревность
# s1, s2 = input().split()
# dct1 = {}
# dct2 = {}
# print(s1, s2)
# for k in s1:
#     if k not in dct1:
#         dct1[k] = 0
#     dct1[k] += 1
# for k in s2:
#     if k not in dct2:
#         dct2[k] = 0
#     dct2[k] += 1
# print(dct1 == dct2)

# #верность ревность
# s= input().split()
# dct1 = {}
# dct2 = {}
#
# for k in s[0]:
#     if k not in dct1:
#         dct1[k] = 0
#     dct1[k] += 1
# for k in s[1]:
#     if k not in dct2:
#         dct2[k] = 0
#     dct2[k] += 1
# print(dct1 == dct2)


# a = (1,2,3)
# #a[0] = 111 нельзя!!!! кортеж неизменяем
# print(a[0:3])

# lst = [11,22,33,44,55,66,77]
# for k, v in enumerate(lst):
#     print(k, v)

# lst = [11,22,33,44,55,66,77]
# for x in enumerate(lst):
#     print(x)
#     print(x[0], x[1])

# tpl = (1,2,3,[11,22,33])
# tpl[3].append(44)
#
# print(tpl)

tpl1 = (123, 234, 345, 456, 567, 678, 789, 890)
x = int(input())
res = 0
if x <= tpl1[0]:
    res = (x,) + tpl1
elif x >= tpl1[-1]:
    res = tpl1 + (x,)
else:
    for k, v in enumerate(tpl1[1:], 1):
        if x <= tpl1[k-1] and x <= v:
            res = tpl1[:k] + (x,) + tpl1[k:]
            break
print(res)

