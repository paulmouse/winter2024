 # Задача 1-2
# Ввести два числа x и y.
# Напечатать наибольшее из чисел x + y, x – y, x*y, x/y, x//y

x = float(input("Число Х:"))
y = float(input("Число Y:"))
#
#
#
# max = x * y # предполагаем, что поизведение самое большое и присваиваем новой переменной значение произведения
#
# if max < (x + y):   # проверим, а вдруг сумма больше?
#     max = (x + y)   # и если сумма больше, то тогда переменная max - это сумма
# if max < (x - y):   # проверим, а вдруг разница больше (например при отрицательном Х или Y)?
#     max = (x - y)   # и опять переопределим переменную max
# if y !=0:           # проверим, не ноль ли y. К сожалению, на 0 не делим((((
#     if max < (x / y):
#         max = (x / y)
# if y !=0:           # и цельночисленно тоже не делим
#     if max < (x // y):
#         max = (x // y)
#
# print(f'Наибольшее выражение даст результат: {max}')
# # print(x * y)
# # print(x + y)
# # print(x - y)
# # print(x / y)
# # print(x // y)

n1, n2, n3, n4, n5 = x * y, x + y, x - y, x / y, x // y
m = n1

if n2 >= m: m = n2
if n3 >= m: m = n3
if n4 >= m: m = n4
if n5 >= m: m = n5
print(n1, n2, n3, n4, n5)
print(m)
