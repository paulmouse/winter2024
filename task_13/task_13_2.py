# Задача 13-2
# Создайте функцию-генератор, которая создает последовательность
# числовых палиндромов:
# 1 2 3 4 5 6 7 8 9 11 22 33 44 55 66 77 88 99 101 111 121 131 141 151
# 161 171 181 191 202 212…

# n = 100
def func1():
    num = 1
    while True:
        if str(num) == str(num)[::-1]: # Строка в обратном порядке - это очень круто)
            yield num
        num += 1

seq = func1()

for i in seq:
    print(i, end=',')
    if i >= 3000:
        break