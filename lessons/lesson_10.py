# f = open('../files/test_10.txt','r', encoding='UTF-8')
# s = f.read()
#s = f.readlines()
#s = f.readline()
# print(f.read(6)) # без отношению к строкам просто символы в файле
#print(s)
# for i in range(len(s)):
#     print(i, len(s[i]), s[i])
#print(f.readlines())

# for i in range(5):
#     print(f.readline().strip())

# f = open('../files/test_10.txt','r', encoding='UTF-8')
# for i in range(10):
#     print(i+1, f.readline().strip())
# f.close()
# f = open('../files/test_10.txt','r', encoding='UTF-8')
# for j, line in enumerate(f):
#     print(j, line.strip())

# fOut = open('../files/test_10.txt','w', encoding='UTF-8')
# fOut.write('testStr1')
# fOut.write('\ntestStr2')
# fOut.close()
#
# f = open('../files/test_10.txt','r', encoding='UTF-8')
# for j, line in enumerate(f):
#      print(j, line.strip())
# f.close()

# f = open('../files/test_10.txt','w', encoding='UTF-8')
# s = ['пишем новую линию\n', 'и вторую\n']
# f.writelines((s))
# f = open('../files/test_10.txt','r', encoding='UTF-8')
# for j, line in enumerate(f):
#       print(j, line.strip())

# fileInput = open('../files/test.txt','r', encoding='UTF-8')
# s = fileInput.readlines()
# fileInput.close()
#
# fileOutput = open('../files/test_1.txt','w', encoding='UTF-8')
# for i in s:
#       for j in i:
#             if j.isdigit():
#                   fileOutput.writelines(i)
#                   break  # это делаем на тот случай, если в строке несколько цифр
# fileOutput.close()
# fileInput = open('../files/test_1.txt','r', encoding='UTF-8')
# for j, line in enumerate(fileInput):
#        print(j, line.strip())

# fileInput = open('../files/test.txt','r', encoding='UTF-8')
# s = fileInput.read()
# for i in s[::2]:  # опять срезы! таким образом получаем каждый второй символ
#       print(i)
# fileInput.close()

# fileInput = open('../files/test.txt','r', encoding='UTF-8')
# s = fileInput.read()
# fileInput.close()
#
# fileOutput = open('../files/test_1.txt','w', encoding='UTF-8')
# for i in s:
#     print(i, file=fileOutput, end='') # печать сразу в файл

# with open('../files/test_1.txt','r', encoding='UTF-8') as f:
#     print(f.readlines())

# with open('../files/test_1.txt','r', encoding='UTF-8') as f:
#     s = f.readlines()
#     with open ('../files/test.txt','w', encoding='UTF-8') as f2:
#         for i in s:
#             w = ' '.join(sorted(i.split()))
#             #print(w)
#             print(w, file=f2, end='\n')
#
#     print(sorted(s))

import openpyxl





