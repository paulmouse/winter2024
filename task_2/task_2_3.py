# Задача 2-3
import math
fact = 1                                            # факториал 0 принимаем за 1
#num = int(input('Введите число:'))
num = 17
for x in range(1, num+1):
    fact = fact*(x)
print(f'Факториал для {num}: {fact}')

print('Отладочное значение:', math.factorial(num))

