# Дано целое число.
# Сосчитать и напечатать, сколько в его записи нулей, единиц, двоек и т.д.
# Например:
# Ввод: 133244459

a = int(input('целое число:'))
strA = str(a)

s0 = strA.count('0')
s1 = strA.count('1')
s2 = strA.count('2')
s3 = strA.count('3')
s4 = strA.count('4')
s5 = strA.count('5')
s6 = strA.count('6')
s7 = strA.count('7')
s8 = strA.count('8')
s9 = strA.count('9')

print(f'0-{s0}')
print(f'1-{s1}')
print(f'2-{s2}')
print(f'3-{s3}')
print(f'4-{s4}')
print(f'5-{s5}')
print(f'6-{s6}')
print(f'7-{s7}')
print(f'8-{s8}')
print(f'9-{s9}')


