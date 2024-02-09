# Задача 11 3
# Напишите функцию, которая переводит арабские числа в римские.
# Например: 2023 -->MMXXIII

romans = {1000:'M',
          500:'D',
          100:'C',
        50:'L',
          10:'X',
          5:'V',
          1:'I'}
def arabToRoman(arabVal):
    romanVal = ''
    while arabVal > 0:
        #print(arabVal)
        for i, r in romans.items():
            while arabVal >= i:
                #print(arabVal)
                romanVal += r
                arabVal -= i
    return romanVal

print(arabToRoman(2027))