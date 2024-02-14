# Задача 12-2
# Создайте списковое включение, которое генерирует следующую
# последовательность:
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, и т.д. до 10

def numCountNum(num):
    numLine = []
    numLineSplit =[]
    # numLine = [(str(x)*x).split(',') for x in range(1, num+1)]
    # numLine = [(str(x) * x) for x in range(1, num + 1)]
    numLine = [x for x in range(1, num +1) for j in range(x)]
    print(numLine)
    # numLineSplit = [x.split() for x in numLine]
    #print(numLineSplit)
    # numLineJoin = ''.join(numLine) # собрали в одну строку
    # print(numLineJoin)
    # for i in numLineJoin:
    #     # if i < 10:
    #     numLineSplit.append(i)
    # numLineSplit = list(numLineJoin) #а теперь строку в лист, чтоб было  через запяттую. Но работает только для цивр. 10 никак(
    # print(numLineSplit)
numCountNum(10)-+