# На вход подаётся предложение из нескольких слов

str1 = 'На вход подаётся предложение слово буква поливинилхлорид'

lst1 = str1.split()
print(max(lst1, key=len), len(max(lst1, key=len)))

# max = 0
#
# for i in lst1:
#     if len(i) > max:
#         max = len(i)
# print(i, max)
