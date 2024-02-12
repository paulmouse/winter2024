# s = [i**2 if i % 2 == 0 else i**3 for i in range(1, 10+1)]
# print(s)

# import functools

# print(functools.reduce(lambda x,y: x+y, [1,2,3,4,5])) #последовательное сложение
# print(functools.reduce(lambda x,y: x*y, [1,2,3,4,5], 10)) #последовательное перемножение

# from functools import cmp_to_key
#
# x = sorted(['d', 'cc', 'bbb', 'aaaaa'])
# def cmp_str(p, q):
#     if len(p)==len(q):
#         return 0
#     elif len(p)< len(q):
#         return -1
#     else: return 1
#
# print(*sorted(x, key = cmp_to_key(cmp_str ))) # cmp_str вызывается без параметров
#
# # print(x)

# import itertools

# for k in itertools.combinations(['f','h','j'], 2):  # все доступные комбинации
#     print(k)
#
# for k in itertools.combinations_with_replacement(['f','h','j', '3','2'], 2):  # все доступные комбинации но с повторам
#
#     print(k)

# for k in itertools.combinations([1,2,5,10], 3):  # все доступные комбинации
#     print(sum(k))
#
# for k in itertools.combinations([1,1,2,2,5,5,10,10], 3):  # все доступные комбинации
#     print(sum(k))

# x = int(input())
# print(x)

# try:
#     s = 1 / 0
#     print('try', s)
# except ValueError:
#     print('Value Error!!!')
# except ZeroDivisionError:
#     print('Zer Division Error!!!')
# except Exception:
#     print('Exception')
# else:
#     print('else', s)
# finally:
#     print('final')


# counter = 0
# while True:
#     try:
#         x = int(input('Введите целое число:'))
#         print(x)
#         break
#     except ValueError:
#         print(f'ValueError - повторите ввод. Попыток осталось: {2-counter}')
#         counter +=1
#         if counter >2:
#             break
# try:
#     with open('files/empData.txt') as f:
#         s = f.read()
#         print(f'Файл найден: {f}')
#
# except FileNotFoundError:
#     print(f'Файл не существует!')

# def func1(n):
#     for x in range(n):
#         # print('before', x)
#         yield x * x
#         # print('after', x)
# g = func1(5)  # создание генератора
# # print(g)
# # for k in g:  # пинаем циклом генератор, и он отдаёт все возможные значения
# #     print(k)
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# for i in g:
#     print(i)


# def funcSqrtCubic(n):
#     for x in range(1, n+1):
#         if x % 2 == 0:
#             yield  x, x ** 2
#         else:
#             yield  x, x ** 3
#
# g = funcSqrtCubic(int(input()))
#
# # for i in g:
# #     print(i)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         print('Конец работы генератора')
#         break

# lim = int(input('Limit:'))
# def fact():
#     f, k =1, 1
#     while True:
#         yield f
#         k += 1
#         if k > lim:
#             break
#         f *= k
# gf = fact()
#
# for i in gf:
#     print(i)


# lst = [1, 10,100,2,20,200,]
# def summa(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#         yield sum
#
# summ = summa(lst)
#
# for y in summ:
#     print(y)



# def br(value, maxRepeat):
#     count = 0
#     while True:
#         if count >= maxRepeat:
#             return 'eee'
#         count += 1
#         yield value
#
# for x in br('qqq', 2):
#     print(x)

def gen(n):
    i = 0
    for i in range(1, n+1):
        yield [i]*i

gener = gen(int(input()))

for i in gener:
    print(*i)













