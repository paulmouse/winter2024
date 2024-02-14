# def div(x,y):
#     return x/y
# try:
#     result = div(100,0)
#     print('ok')
# except (ZeroDivisionError, KeyError) as e:
#     print('Ошибка:', e)

# def div(x,y):
#     return x/y
# try:
#     result = div(100,0)
#     print('ok')
# except (ZeroDivisionError) as e:
#     print('Ошибка деления:', e)
# except KeyError as g:
#     print('ошибка ключа', g)

# def divide(x, y):
#     try:
#         out = x/y
#     except:
#         try:
#             import math
#             out = math.inf * x/abs(x)
#         except:
#             out = None
#     finally:
#         return out
#
# print(divide(-0,0))


# try:
#     raise Exception('Error')# принудительный вызов ошибки. Поднятие Exeption b уход в except
# except Exception as e:
#     print('Message: '+ str(e))

# def validate(name):
#     if len(name)<10:
#         raise ValueError
#     else:
#         print('Ok')
#
# try:
#     name = input('Введите имя')
#     validate(name)
# except ValueError:
#     print('Чо так мало то?')

# class NameToShortError(ValueError): # наследуем от valueError создавая своё исключение
#     pass
#
#
# def validate(name):
#     if len(name)<10:
#         raise NameToShortError(name)
#     else:
#         print('Ok')
#
# try:
#     name = input('Введите имя')
#     validate(name)
# except NameToShortError as e:
#     print('Чо так мало то?', e)

# class NegValExp(Exception):
#     pass
#
# try:
#     val = int(input('only positive:'))
#     if val < 0:
#         raise NegValExp("Negative value:"+ str(val))
#     print(val + 10)
# except NegValExp as e:
#     print(e)

# class OnlyLetters(Exception):
#     pass
# class OnlyDigits(Exception):
#     pass
#
# try:
#     password = (input('Придумайте пароль:'))
#     if password.isdigit():
#         raise OnlyDigits('Тут только цифры! не пойдёт :' + str(password))
#     elif password.isalpha():
#         raise OnlyLetters('Тут только буквы! не пойдёт давай еще цифр :' + str(password))
#     else:
#         print('Пароль ок')
# except OnlyDigits as e:
#     print(e)
# except OnlyLetters as e:
#     print(e)

# def fun(n):
#     for x in range(n):
#         yield x * x
# g = fun(6)
# for _ in range(10):  # _ можно использовать если не нужно само значение, а только генератор например
#     try:
#         print(next(g))
#     except StopIteration:
#         break

# def bounder_repeater(value, max_repeats):
#     count = 0
#     while True:
#         if count >= max_repeats:
#             return
#         count += 1
#         yield value
#
# for x in bounder_repeater('Раз', 3):
#     print(x)

# def repeater123():
#     yield 1
#     yield 2
#     yield 3
# print(*repeater123()) # Распаковать значения
# print(2 in repeater123()) # Использовать функцию in
# n1, n2, n3 = repeater123() # Множественное присвоение значений
# print(n1, n2, n3)


# def repeater123():
#     yield 1
#     yield 2
#     yield 3
#
# gen = repeater123()
# print(*gen)
# print(2 in gen)
# print(1 in gen)
# print(1 in repeater123())
# print(1 in gen)

# def fun_gen(n):
#     for x in range(n):
#         yield x
# for i in fun_gen(5):
#     print(i)
# # Можно упростить
# def fun_gen2(n):
#     yield from range(n)
# for i in fun_gen2(5):
#     print(i)


# def funGen3():
#     yield  from 'abcdef'
# print(*funGen3())
# # Например:
# # yield from ‘abcdef’
# # yield from [ 11, 22, 33, ‘abc’, {1:111}]

# def fun_gen1():
#     yield "Красный"
#     yield "Зеленый"
#     yield "Синий"
# def fun_gen2():
#     yield "Круглый"
#     yield from fun_gen1() # генератор вызывает генератор
#     yield "Квадратный"
# print(*fun_gen2())

# lc = [x for x in range(10)]
# print(*lc)
# ge = (x for x in range(10))
# print(*ge)
# print(ge)


# def integers(n):
#     yield from range(1, n + 1)
#         # yield i
# def evens(iterable):
#     for i in iterable:
#         if not i % 2:
#             yield i
# def squared(iterable):
#     for k in iterable:
#         yield k * k
# chain = squared(evens(integers(10)))  #называется конвеер
# print(*chain)


# def charNum():
#     yield from range(65, 91)
# def chrVal(iterable):
#     for i in iterable:
#         yield chr(i)
#
# print(*chrVal(charNum()))
# print(*charNum())

# def func():
#     print('func')
#     input()
#     func()
# func()

# def func(n):
#     print('func1 n =', n)
#     input()
#     n -= 1
#     if n > 0:
#         func(n)
#     print('func2 n =', n)
#     input()
#     return # ничего не делает, возвращает на строку после запуска функции на  print('func2 n =', n)
# func(3)


# def fact(n):
#     if n == 1:
#         return 1 # базовый случай – вариант решения
# # без рекурсии
#     else:
#         return n * fact(n - 1) # рекурсивный случай – сведение задачи к более простой
# print(fact(1))
# print(fact(2))
# print(fact(6))

# def triangle(n):
#     if n == 1:
#         print('*') # базовый случай – вариант решения
#         return
# # без рекурсии
#     else:
#         print('*' * n)
#         triangle(n-1) # рекурсивный случай – сведение задачи к более простой
# triangle(5)

# def summ(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
# # без рекурсии
#     else:
#         return n + summ(n-1) # рекурсивный случай – сведение задачи к более простой
# print(summ(100))

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
# без рекурсии
    else:
        return fibo(n-1)+fibo(n-2) # рекурсивный случай – сведение задачи к более простой
print(fibo(6))


