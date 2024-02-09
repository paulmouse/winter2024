# import time, math
# t0 = time.time()
# print(t0)
# for i in range (1, 3000, 100):
#     s = 0
#     for j in range(1,i):
#         s += math.factorial(j)
#     t1 = time.time()
#     print(i, t1-t0)

# import datetime, locale
# locale.setlocale(locale.LC_ALL, 'ru')
# a = datetime.datetime.today() + datetime.timedelta(days=7)
# c = datetime.timedelta(days = 1)
# for _ in range(10):
#     a += c
#     print(a.strftime('%A %d, %B %Y'))
#
# from datetime import datetime
# print(datetime.strptime('09 02 2024 19:34:12', '%d.%m.%Y'))

# from calendar import calendar
#
# print(calendar(2024, w=2,l=1,c=6, m =3))
#
# import calendar
# year, month = tuple(map(int, input().split()))
# print(calendar.monthcalendar(year,month))


# import itertools
# # for i in itertools.chain('abc', [11,22,33,44], {1:11, 2:22}, (True, False, None)):
# #     print(i)
# # for i in zip('abc', [11,22,33,44], {1:11, 2:22}, (True, False, None)):
# #     print(i)
# for i in itertools.zip_longest('abc', [11, 22, 33, 44], {1: 11, 2: 22}, (True, False, None), fillvalue=0):
#     print(i)
#
# def flipFlop(x):
#     return 'flip' if x =='flop' else 'flop'
#
# print(flipFlop('flop'))

# list comprehansion
# lst = [x**2 for x in range (0, 10) if x % 3 == 0]
# print(lst)
# циклом
# lst1 = []
# for x in range(10):
#     if x % 2 ==0:
#         lst1.append(x**2)
# print(lst1)
# # list map lambda
# lst2= list(map(lambda x: x**2, range(10)))
# print(lst2)
# # list comprehansion
# lst3 = [x**2 for x in range (0, 10) if x % 3 == 0]

# lst4 = [x for x in range(21) if x %2 ==0]
# print(lst4)
# lst5 = [x**2 if x %2 ==1 else x**3 for x in range(10)]
# print(lst5)
# op =[1.25, -9.45, 10.22, 3.78, -5.23]

# from string import ascii_letters
# letters = 'jcifsdlllолыоваашвьjdsudidk'
#
# iseng = [f'{let} - ДА' if let in ascii_letters else f'{let} - НЕТ' for let in letters]
# print(iseng, sep='/n')


# inp = 'God save the Queen'
#
# a = [x for x in inp if x.lower() in 'aouei']
# # a = set([x for x in inp if x.lower() in 'aouei']) #set
# # a = {x for x in inp if x.lower() in 'aouei'}  #set
#
# print(a)

# op =[1.25, -9.45, 10.22, 3.78, -5.23]
#
# a = [0 if x<0 else x  for x in op]
# print(a)

# fizzBuzz = ['FB' if x % 15 == 0 else 'F' if x % 3 ==0 else 'B' if x % 5 ==0 else x for x in range(31)]
# print(fizzBuzz)

# words = ['я', 'изучаю','python']
# res2 = [s for w in words for s in w]
#
# res = []
# for w in words:
#     for s in w:
#         res.append(s)
# print(res, res2)

# key = ['name', 'age', 'weight']
# value = [11,22,33]
# res = [{k,v}for k in key for v in value]
# print(res)

# 2 x matrix
# m = [[i**j for i in range(5)] for j in range(5)]
# for s in m:
#     print(s)

# двумерная в одномерную

# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]
# ]
# flat = [num for row in m for num in row]
# print(flat)

# t = [[x * y for x in range(1, 10)] for y in range(1,10)]
# print(t)

# lst = list(map(int,input().split()))
# lst2 = [int(x) for x in input().split()]
# print(lst2)

# a = [x for x in range(10000)]
#
# b = (x for x in range(10))
#
#
# # print(a, b)
# print(type(a), type(b))
# import sys
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# d = {k:k**2 for k in range(1,10)}
# print(d)

lst = [('c', 3), ('d', 4)]
# d = {key:val for (key,val) in lst }
d = {key:val for (key,val) in lst if val % 2 == 0}
print(d)
