# Задача 20 2
# Напишите функцию, которая на вход получает DataFrame , который
# содержит числа и строки, а в качестве результата возвращает
# сумму всех чисел.

import pandas as pd
import numpy
dataframe = pd.DataFrame({
'Год': [2001, 2002, 2003, 2004, 2005],
'Товар': ['A','B','C','D','E'],
'Описание': ['Товар А', 'Товар V', 'Товар R', 'Товар F', 'Товар S'],
'Цена': [100, 50, 30, 40, 5]})

def numericSum(dataframe):
    total = 0
    for i in dataframe.index:
        for j in dataframe.columns:
            val = dataframe.loc[i,j]
            if isinstance(val, numpy.int64):
            # if type(val) == numpy.int64:  # не идеально фильтруем только не строки. Но с этими типами данных isinstace не работает(
                # print(type(val))
                # print(val)
                total += val
                # print(total)
    # return val
    return total

funcResult = numericSum(dataframe)
print(funcResult)