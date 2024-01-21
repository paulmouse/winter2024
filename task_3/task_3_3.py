# На вход подаётся предложение из нескольких слов

str1 = 'На вход подаётся предложение'

lst1 = str1.split()
max = 0

for i in lst1:
    if len(i) > max:
        max = len(i)
print(i, max)
