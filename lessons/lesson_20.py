# import itertools
# for x in itertools.permutations ([1,2,3]):
#     print(x, end = '')
# # (1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1)

# for x in itertools.combinations ([1,2,3,4],2):
#     print(x, end = '')
# (1, 2, 3) (1, 2, 4) (1, 3, 4) (2, 3, 4)

# for x in itertools.combinations_with_replacement ([1,2,3,4],2):
#     print(x, end = '')


# x = itertools.cycle ([1,2,3,4])
# for _ in range(10):
#     print(next(x))

# x = itertools.chain ([1,2,3,4], 'abcd')
# for _ in range(7):
#     print(next(x))

# list(zip([1, 2, 3], [11, 22, 33, 44])) # [(1,11), (2,22), (3,33)]
# list(itertools.zip_longest ([1, 2, 3], [11, 22, 33, 44], fillvalue =None))
# #


# s = 'aaabbbaaaaabbcccccd'
# for k, v in itertools.groupby(s):
#     print(k, ':', *v)
#
# s = 'aaa123bbbaaaaa345bbcccccd'
# for k, v in itertools.groupby(s, key=lambda x: x.isdigit):
#     print(k, ':', *v)
#
# def odd(x):
#     return x % 2
# s = [1,2,4,6,3,3,10,8,4]
# for k, v in itertools.groupby(s, odd):
#     print(k,':', *v)

# s = [-1, -2, 3, 1,-2,-3,4, -10, 7, 5, 0]
# for k, v in itertools.groupby(s, key=lambda x: x>0):
#     print(k, ':', *v)#<itertools._grouper object
#




# import numpy as np
# lst = [[1,11,111],[2,22,222]]
# arr = np.array(lst)
# # print(arr.shape)
# print(arr)

# a1 = np.array ([1, 2,])
# a2 = np.array ([10, 20,])
# print(a1 + a2)

# a = np.zeros ((2,3), dtype =int)
# print(a)
# print(a.shape)
# b = a.reshape(6)
# print(b)
# print(b.shape)

# a1 =np.array([[1, 2, 3], [10, 20,30]])
# print(np.sum(a1))
# print(np.sum(a1, axis=None)) # А если вместо None поставить 0? А если 1?
# print(np.prod(a1, axis=None)) # А если вместо None поставить 0? А если 1?

# print(np.gcd([6,24,72], [24,12,36]))
# print(np.lcm([6,24,72], [24,12,36]))

# import numpy as np
# import matplotlib.pyplot as plt
# x = np.linspace(-2, 5, num=50)
# y = np.exp (x) # * 100
# plt.plot(x,y)
# plt.grid()
# plt.savefig('123.jpg')
# _ = plt.title('exp')
# plt.show()

# import numpy as np
# # x = np.array([1,2,3,5,6,7,8,9,])
# # x = np.array([1,2,3,5,6,7,8,9,np.nan])
# # print(np.mean(x))
#
# # x = np.array([1,2,3,5,6,7,8,9,])
# x = np.array([1,2,3,5,6,7,8,9,10])
# print(np.percentile(x, 50))  #Q - то процент. Регулируемая медиана. 50 означает что 50% значений с одной стороны и 50 с другой от значения

# import numpy as np
# a1 =np.array ([1, 2, 3])
# a2 =np.array ([2, 2, 2])
# print(a1 > a2)
# x = a1==a2
# print(a1[x])

# import numpy as np
# arr = np.array ([2, 7, 7, 8, 8, 6, 8, 7, 6,])
# condition = arr < np.percentile(arr, 40)  # это true or False
# print(arr[arr < np.percentile (arr , 40)]) #
# print(arr[condition])
#
# Поиск, сортировка, выборка
# import numpy as np
# # x = np.array([3,5,1,8,13,4])
# # y = x*10
# # print(x)
# # print(y)
# # print(np.where(x>9,x,y))
#
# x = np.array([[3,5,1,8],[13,4,5,7]])
#
# print(np.sort(x,axis=1))

# import pandas as pd
# df1 = pd.DataFrame ([[1,'Bob', 'Builder'], # из двумерного списка
#                         [2,'Sally', 'Baker'],
#                         [3,'Scott', 'Candle Stick Maker']],
# columns=['id','name ', 'occupation'])
# print(df1) # Выполните
#
# df2 = pd.DataFrame ({
# 'country': ['Kazakhstan', 'Russia', 'Belarus', 'Ukraine'],
# 'population': [17.04, 143.5, 9.5, 45.5],
# 'square': [2724902, 17125191, 207600, 603628]})
# print(df2)# Выполните
# lst = {'id':['First', 'Second', 'Third'],
#        'num':['1', '2', '3']}
# df3 = pd.DataFrame(lst)
# print(df3)
# df3['xxx'] = df3['id']+df3['num']
# print(df3)
# df3['qqq'] = [123,456,789]
# print(df3)
# import pandas as pd
# import matplotlib.pyplot as plt
# df = pd.DataFrame({
# 'Год': [2001, 2002, 2003, 2004, 2005],
# 'Товар': ['A','B','C','D','E'],
# 'Количество': [10, 20, 30, 40, 50],
# 'Цена': [100, 50, 30, 40, 5]})
# # print(df)
# df['Итого'] = df['Количество']*df['Цена']
# print(df)
# # df.to_excel('test.xlsx')
# df1 =pd.DataFrame()
# df1['Год'] = df['Год']
# df1['Итого'] = df['Итого']
# print(df1)
# df1.index = df1['Год']
# df1['Итого']. plot(kind='barh')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
'Год': [2001, 2002, 2003, 2004, 2005],
'Товар': ['A','B','C','D','E'],
'Количество': [10, 20, 30, 40, 50],
'Цена': [100, 50, 30, 40, 5]})
# print(df)
df['Итого'] = df['Количество']*df['Цена']

# print(df)
# print(df['Количество'])
# print(df[['Количество', 'Год']])
# df.index = df['Год']
# print(df.iloc[0:3])
# print(df.loc[2003:2005])
# print(df.index)
# print(df.columns)
for i in df.index:
    for j in df.columns:
        print (i,j, df.loc[i,j])
# print(df[(df['Год'] == 2001]))
