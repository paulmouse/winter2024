# # сортированый список
# print(sorted([1, 2, 3, 4, 5]))
#
# # ключ абс не даёт обращать внимание на знак
# print(sorted([1, -2, 3, 4, -5], key = abs))

# import math
# print(math.sqrt(9))
# print(math.pi)

# # Импортируем из модуля math функцию sqrt
# from math import sqrt
# # Выводим результат выполнения функции sqrt.
# # Обратите внимание , что нам больше незачем указывать имя модуля
# print (sqrt(144))
# # Но мы уже не можем получить из модуля то , что не импортировали
# print(pi) # Выдаст ошибку

# Импортировать из модуля объекты можно через запятую
# from math import pi, sqrt
# print(sqrt(9))
# print(pi)

# Некоторые функции из math
# Тригонометрия: acos acosh asin asinh atan atan2 atanh cos cosh sin sinh tan tanh degrees radians
# Округления: ceil floor trunc
# Экспонента и логарифмы: exp log log10 log1p log2
# Арифметика: dist remainder sqrt factorial gcd isqrt pow prod fsum
# Великие постоянные: e pi inf nan isinf isnan isfinite

# За один раз можно импортировать сразу несколько модулей ,для этого их нужно перечислить через запятую после слова import
# import math, os
# print(math.sqrt(9))
# print(os.environ)

# Если вы хотите задать псевдоним для модуля в вашей программе, можно воспользоваться вот таким синтаксисом
# import math as matan
# print(matan.sqrt(199))


# Лямбда функции, анонимные функции
# Раньше мы использовали функции , обязательно связывая их с каким-то именем.
# В Python есть возможность создания однострочных анонимных функций
# Конструкция:
# lambda[param1, param2, ..]:[выражение]
# lambda - функция, возвращает свое значение в том месте, в котором вы его объявляете

# Пример
# def fun1(x):
#     return x % 10
# spi=[222, 21, 1, 111, 12, 322]
# print(sorted(spi, key=fun1))
# print(sorted(spi, key=lambda x: x % 10))