# Задача 2-1

num = int(input('Введите число:'))
print(f'Строим таблицу умножения для числа {num}:')
for x in range(1,9+1):
    print(f'{x} x {num} = {x*num}')