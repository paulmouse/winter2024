# Задача 12-2
# Создайте списковое включение, которое генерирует следующую
# последовательность:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

def numCountNum(num):
    numLine = []
    # numLine = [(str(x)*x).split(',') for x in range(1, num+1)]
    numLine = [(str(x) * x) for x in range(1, num + 1)]
    print(numLine)
    # numLineSplit = [x.split() for x in numLine]
    # print(numLineSplit)
    numLineJoin = ''.join(numLine)
    print(numLineJoin)
    numLineSplit = list(numLineJoin)
    print(numLineSplit)
numCountNum(5)