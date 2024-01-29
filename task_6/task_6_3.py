# Задача 6-3
# Напишите программу, которая принимает на вход строку из
# символов и печатает одну строку из букв, вторую из цифр, третью
# из прочих символов без повторений.
# Например:
# Ввод: ab18.,cab=561:xz:
# Вывод:
# a b c x z
# 1 8 5 6
# . , = :

s = input()
sSet = set(s)
letterSet = set()
digitSet = set()
simbolSet = set()

for k in sSet:
    if k.isdigit():
        digitSet.add(k)
    elif k.isalpha():
        letterSet.add(k)
    else:
        simbolSet.add(k)


print(letterSet)
print(digitSet)
print(simbolSet)
