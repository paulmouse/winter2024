# Задача 15-2
# Напишите функцию, которая принимает строку символов, и
# печатает все содержащиеся в ней номера автомашин по
# следующему правилу:
# LDDDLL78 или LDDDLL178,
# где L – буквы, совпадающие по начертанию в русском и латинском
# алфавите, D – цифры от 0 до 9.
# Например, A123BC78 или X666XX178
#А, В, Е, К, М, Н, О, Р, С, Т, У и Х кириллица
# A, B, E, K, M, H, O, P, C, T, Y, X
import re
# inputString = 'H267BE178 M439KX177 X230EU78 C4286O178 Y349AY123 H494BX78'
inputString = 'H267BE178 M439KX177 H233TC178 X230EU78 C4286O178 Y349AY123 H494BX78'
# regex = r'\b\w{1}[ABEKMHOPCTYX]\d{3}\w{2}[ABEKMHOPCTYX]\d{2,3}[178]\b'
regex = r'\b[ABEKMHOPCTYX][0-9]{3}[ABEKMHOPCTYX]{2}178\b|\b[ABEKMHOPCTYX][0-9]{3}[ABEKMHOPCTYX]{2}78\b'

print(re.findall(regex,inputString))