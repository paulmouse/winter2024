# print(1, 2, 3, sep=' ', end=' ')
# print(4)
#--------

# for i in 'Hello world':
#     print(i, end='')

# for i in range(10+1):
#     if i % 2 == 0:
#         print(i, '- чётное')
#     else:
#         print(i,'- нечётное')
#     # print(i, i*i, i**2)

# FizzBuzz
# n = 21
# for i in range(1, n+1):
#     if (i % 5 == 0) and (i % 3 == 0):
#         print(i,'FizzBuzz')
#     elif i % 5 == 0:
#         print(i, 'Buzz')
#     elif i % 3 == 0:
#         print(i, 'Fizz')
#     else:
#         print(i)
# FizzBuzz

# for i in range(1, 12+1):
#     if i % 15 == 0: break
#     if i % 2 != 0: continue # переход на новое значение цикла
#     print(i)
# else:
#     print('Normal end')

# for i in 'Hello world':
#     if i == 'a':
#         break
# else:
#     print('letter is not in srting')

# n = 15
# for i in range(n+1):
#     if i > 10:
#         break
#     elif i % 2 == 0:
#         continue
#     else: # здесь else относится к if а не циклу for
#         print(i)

# s = 'Hello World'
# print(s[0]) # указываем какой символ брать
# print(s[0:10]) # подстрока


# лесенка из символов
# for i in range(1,10):
#     for j in range(i):
#         print('+', end='')
#     print()
# лесенка из символов


# a = [1, 2, 3, [23, 24], 'test', 'alt']
# for i in a:
#     print(i)

# s = list('Hello')
# # print(s)
# # s[0] = 123
# # print(s)


# два способа вытащить список
# mass = [1,2,3,45,66,78,99]
# for j in mass:
#     print(j)
#
# for j in range(len(mass)):
#     print(mass[j])

# inputList = [10, 12, 'aaa', 111, 'd']
#
# for x in inputList:
#     if type(x) == str:
#         print(f'String {x}')
#     elif type(x) == int:
#         print(f'Integer {x}')

lst = []
for i in range(5):
    a = int(input())
    lst.append(a)
print(lst)