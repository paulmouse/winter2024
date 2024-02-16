# Задача 14-1
# • Напишите рекурсивную функцию, которая вычисляет количество
# цифр введенного целого числа n (n >= 0).

def digitCount(s, c):
    if s > 0:
        s = int(s / 10)
        # print(s)
        c += 1
        # print('c:',s, c)
    if s > 0:
        c = digitCount(s, c)
        return c
    else:
        return c
c = 0
print('return:', digitCount(123123123123, c))

# def digitCount(s, c):
#     if len(s) > 0:
#         s = s[:-1]
#         # print(s)
#         c += 1
#         # print('c:',s, c)
#     if len(s) > 0:
#         c = digitCount(s,c)
#         return c
#     else:
#         return c
# c = 0
# print('return:', digitCount(str(123123123123), c))





# решение без рекурсии
# def digitCount(n):
#     x = len(str(n))
#     # print(x)
#     return x
# print(digitCount(334534535))
# решение без рекурсии
