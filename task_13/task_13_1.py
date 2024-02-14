# Задача 13-1
# Создайте функцию-генератор, которая создает бесконечную
# последовательность:
# 1, -2, 3, -4, 5, -6, …
n = 10
def func1(n):
    num = 1
    while num <= n:
        yield num
        yield -num-1
        num += 2

seq = func1(n)

for i in seq:
    print(i, end=',')