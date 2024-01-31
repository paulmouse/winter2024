# Задача 7-2
# Напишите функцию, которая шифрует строку, содержащую
# латинские буквы с помощью шифра Цезаря. Каждая буква
# сдвигается на заданное число n позиций вправо. Пробелы, знаки
# препинания не меняются.
# Например, для n = 1
# a--> b, b --> c, p --> q, y --> z, z --> a
# A--> B, B --> C, Z -->A
# Т.е. заголовок функции будет def code(string, n):
# В качестве результата печатается сдвинутая строка.

string = 'hello world!'
n = 6676 # веселье начинается, когда n больше 25.....
# nCycle = n-25

#print(ord('a'),ord('b'),ord('c'))
# a = ord('A')
# z = ord('Z')
# print(a)
# print(z)
# print(nCycle)
def code(string, n):
        result = '' # пустая строка для вывода
        for char in string:
             if char.isalpha(): # условие на то, является ли буквой
                 if char.isupper():
                     ordValue = ord('A')
                 else:
                     ordValue = ord('a')
                 charNum = ((ord(char) - ordValue + n) % 26) + ordValue # остаток отделения подсмотрел. инпче никак в диапазоне 65 -122 не оставить
                 result += chr(charNum)
                 #print(char, ord(char))
                 #print(chr(charNum), charNum)
             else:
                result += char
                 # если не буква, просто его к результау
        return result
#
inputText = code(string, n)
print(f'Result: {inputText}')
# Это не сработало...
#                 if ord(char) >= 122 and nCycle <= 0:
#                     charNum = ((ord(char) - 25  + n))
#                     print('run1')
#                     print(char, ord(char))
#                     print(chr(charNum), charNum)
#                 elif ord(char) >= 122 and nCycle > 0:
#                     charNum = (a-1 + nCycle)
#                     print('run2')
#                     print(char, ord(char))
#                     print(chr(charNum), charNum)
#                 else:
#                     charNum = (ord(char) + n)
#                     print(char, ord(char))
#                     print(chr(charNum), charNum)
#                 #print(charNum)
# Это не сработало...