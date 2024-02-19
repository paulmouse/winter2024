# a = [i for i in range(10)]
# b = (i for i in range(10))
# c = {i for i in range(10)}
# d = {x: x**2 for x in range(10)}
# print(c)
# print(print(10))

# def f(x,y):
#     try:
#         return x/y
#     except:
#         return x,y
#     finally:
#         print('finally')
# print(f(1,1))

# def fun_gen():
#     yield from 'abcdef'
# for i in fun_gen():
#     print(i)

# d = {}
# def fact(n):
#     d[n] = d.get(n,0) + 1
#     if n ==1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fact(n-1)+ fact(n-2)
# fact(15)
# print(d)

# d = {}
# res = {1:0,2:1}
# def fibo(n):
#     d[n] = d.get(n,0) + 1
#     if n not in res:
#         if n > 2:
#             res[n] = fibo(n-1) + fibo(n-2)
#     return res[n]
#
# fibo(15)
# print(res)
# print(d)


# lst =  [1, 2, [11, 22, [111, 222, [1111, 'sg', 3333], 333, 'fggg', [555, 666]], 3],4]
# # lst =  [1, 2, [3, 4]]
# res = []
# def numbers(lst):
#     for i in lst:
#         print(i, res)
#         if type(i) == int or type(i) == float:
#             res.append(i)
#         elif type(i) == list:
#             numbers(i)
# numbers(lst)
# print(res)

# import sys
# print(sys.getrecursionlimit())


import re
# s = 'Числа 99, 72, 81 и 999 делятся на 9'
# # print(re.findall(r'\d\s',s))
# print(re.findall(r'[а-я]',s))

# . ^ $ * + ? {} [] \ | () – для их написания их необходимо
# экранировать, т.е. поставить перед ними знак \

# s = '0abracadabra1 abracadabra'
# print(re.findall(r'\da\w|\wa\d',s))
# s = '12773 338267 029 345 437 001 1000 654 sdf'


# regex = r'\d{3}'
# print(re.findall(r'1\d{1}[^\s]',s))

# s = 'Косой косой косил траву на покосе'
# print(re.findall(r'\b\w*[Кк]ос\w*\b',s))

# tn = 'Мой номер телефона 921-921-0477'
# regex = r'\d{3}-\d{3}-\d{4}'
# print(re.findall(regex,tn))

# tn = 'A123BC78 A123BC178 D77FFF234'
# # regex = r'\w{1}\d{3}\w{2}\d{,3}'
# regex = r'\b[A-Z]\d{3}[A-Z]{2}\d{2,3}\b'
# print(re.findall(regex,tn))

# text = 'java самый популярный язык программирования в 2023 году.'
# res = re.sub(r'[Jj]ava', r'Python', text)  # замена что меняем., на что
# print(res)
#
# text = 'java самый популярный язык программирования в 2023 году.'
# res, n = re.subn(r'[Jj]ava', r'Python', text)  # замена что меняем., на что и+ количество замен
# print(res,n )

# text = 'Чётные числа в строке 7 89 2 65 -76 56 43 54'
# regex = r'[+-]?\d*[02468]\b'
# print(re.findall(regex,text))

text = 'Чётные числа в строке 7 55 2 65 -10 56 43 55 350'
regex = r'[+-]?\d*[05]\b'
print(re.findall(regex,text))

