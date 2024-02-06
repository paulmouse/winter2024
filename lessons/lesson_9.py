#
#
#
# (lambda x: x*x)(12)

# print(*list(map((lambda x: x*x), range(10))))
# # * распаковывает список
#
# def sqrtx(x):
#     return x * x
# print(*list(map(sqrtx, range(10))))

# именование lambda
# addOne = lambda x: x+1
# print(addOne(2))

# аргументы к lambda может быть сколько угодно
# fu = lambda x, y, *args, **kwargs : x+y
# print(fu(3,4))


# l1 = lambda s: str(s).lower()[::-1]
# # [::-1] - перевернуть строку
# # [::3] - каждая третья символ
#
# print(l1('DJDFOJDIemdkjkdkd'))
#
# print(max([1,3,4,6,7,-5,-8,-4,5], key = abs))
#
# print(sorted([1,3,4,6,7,-5,-8,-4,5], key = lambda x: x % 2))
# # x % 2 - ключ для сортировки. Или 1 или 0

# print(sorted(['x', 's', 'r', "X"], key = lambda x : (x.lower(), x)))


# lst = [1,10,21,30]
# y = 16
# print(min([1,10,21,30], key = lambda x: abs(x-y)))


# t = (lambda x: x*2, lambda x: x*3, lambda x: x*4)
# y = 10
# for f in t:
#     # print(f(y)) # применение итерирования функции к числу
#
# def any():
#     print('******')
#
#
# dict = {
#     1: (lambda : print('Monday')),
#     2: (lambda : print('Tuesday')),
#     3: (lambda : print('Wensday')),
#     4: (lambda : print('Thuesday')),
#     5: any # без скобок потому что не вызываем
# }
# dict[5]()

# print(list(filter(lambda x: x % 2==0, [1,2,3,4,5,6,7])))

# lst = [123, 234, 345, 456]
# print(list(map(lambda x: sum(map(int, list(str(x))), lst))))
# # sum(map(int, list(str(x))))

# s = [222,31,1,711,82,322]
# print(sorted(s, key = lambda x: int(str(x)[0]))) # сортируем по первой цифре

# тернарный оператор
# x = 4
# y = 2
# maxim = x if x > y else y
# print(maxim)

# lower = (lambda x, y: x if x > y else y)
#
# (lambda x,y: x if x > y else y)(2,4)
# l = lower(3,4)
# print(l)

# pd = (lambda d: d*0.13 if d < 5000000 else 650000 + (d-5000000)*0.15)(5000001)
# pd = (lambda d, lim: d*0.13 if d < lim else lim*0.13+ (d - lim)*0.15)(5000001, 5000000)
# 13
# print(pd)


# lis =[('иванов', 100),('Петров', 100),('Сидоров', 100),('Воробьёв', 50),('Лунин', 100)]
#
# print(sorted(lis, key = lambda x: (-x[1], x[0]))) # оба параметра сортировки в скобки - для получения кортежа

# сортировка по номеру параметра внутри кортежа.


# вложеные словари
# students = {0: {'name': 'Иванов', 'age': 22},
#             1: {'name': 'Петров', 'age': 23},
#             2: {'name': 'Сидоров', 'age': 24}
#             }
#
# for st in students:
#     print(st, students[st])
#     for attr in students[st]:
#         print(attr,students[st][attr] )

# dct = {1: 123, 2:234, 3:{1:111, 2:222},4:{1:'abc', 2:'def'}}
# x = 1
#
# for k, v in dct.items():
#     if k == x:
#         print(v)
#     if type(v) == dict:
#         for a, y in v.items():
#             if a == x:
#                 print(y)

# f = open('../files/test_9.txt', encoding='utf-8')
# s = f.readlines()
# for i in s:
#     print(i.strip())
# # print(s)
# f.close()

# f = open('../files/test_9.txt', 'w', encoding='utf-8')
# for i in range(5):
#     s = input()
#     print(s, file=f)
# f.close()

# f = open('../files/test_9.txt')
# f = open('lesson_9.py', encoding = 'utf-8')
# for i in f:
#     if i[0] != '#' or i[0] == ' ' or i[0] == '\n':
#         print(i.strip())

f = open()
for line in f:
    print(line)


