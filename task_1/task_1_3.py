# Задача 1-3
# Ввести два числа x и y.
# Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ из чисел x + y, x – y, x*y, x/y, x//y

x = float(input("Число Х:"))
y = float(input("Число Y:"))

max = x * y # предполагаем, что поизведение самое большое и присваиваем новой переменной значение произведения
max2 = x * y
# if y !=0:
#     max2 = x // y # предполагаем что цельночисленное (как теоретически самое малое) самое малое
# else:
#     max2 = (x - y) # ну а если У == 0 самое малое разница

# e1 = (x * y)
# e2 = (x + y)
# e3 = (x - y)
# if y !=0:
#     e4 = (x / y)
# if y !=0:
#     e5 = (x // y)
#
# if max < (x + y):   # проверим, а вдруг сумма больше?
#     max = (x + y)   # и если сумма больше, то тогда переменная max - это сумма
#
# if max < (x - y):   # проверим, а вдруг разница больше (например при отрицательном Х или Y)?
#     max2 = max
#     max = (x - y)   # и опять переопределим переменную max
# if y !=0:           # проверим, не ноль ли y. К сожалению, на 0 не делим((((
#     if max < (x / y):
#         max2 = max
#         max = (x / y)
# if y !=0:           # и цельночисленно тоже не делим
#     if max < (x // y):
#         max2 = max
#         max = (x // y)
# print(f'Наибольшее выражение даст результат: {max}')
# print(f'Второе по велечине выражение даст результат: {max2}')

# print(x * y)
# print(x + y)
# print(x - y)
# print(x / y)
# print(x // y)

# начало варианта решения с листом и сортировкой
# list =[]                # создаём пустой список
#
# e1 = list.append(x * y) # поочередно добавляем результаты в список list
# e2 = list.append(x + y)
# e3 = list.append(x - y)
# if y !=0:               # делить на 0 нельзя, поэтому выкидываем эти результаты
#     e4 = list.append(x / y)
# if y !=0:
#     e5 = list.append(x // y)
#
# list.sort(reverse=True) # сортируем список
# #print(list) # для отладки выведем сортированый список
# print(list[1])      # выведем элемент с индексом 1 из списка (второй по величине)
# конец варианта решения с листом и сортировкой


n1, n2, n3, n4, n5 = x * y, x + y, x - y, x / y, x // y
m1 = n1
m2 = 0

if n1 >= n2:
    m1 = n1
    m2 = n2
else:
    m1 = n2
    m2 = n1
if n3 >= m1:
    m2 = m1
    m1 = n3
elif n3 >= m2:
    m2 = n3
if n4 >= m1:
    m2 = m1
    m1 = n4
elif n4 >= m2:
    m2 = n4
if n5 >= m1:
    m2 = m1
    m1 = n5
elif n5 >= m2:
     m2 = n5

print(n1, n2, n3, n4, n5)
print(m1, m2)