import pandas as pd
import matplotlib.pyplot as plt

# a = {'Год':[2001, 2002, 2003, 2004], 'Шт':[1,2,3, 4], 'A':[100, 200, 300, 400]}
# df = pd.DataFrame(a, index = [2001, 2002, 2003, 2004])
# df1 = pd.DataFrame({'Company':['aa', 'bb', 'cc', 'dd']}, index = [2001, 2002, 2003, 2004])
# df2 = df.join(df1)
# print(df2)


# a = {'Год':[2001, 2002, 2003, 2004], 'Шт':[1,2,3, 4], 'A':[100, 200, 300, 400]}
# df = pd.DataFrame(a, index = [2001, 2002, 2003, 2004])
# df1 = df.loc[[2001, 2002]]
# df2 = df.loc[[2003, 2004]]
# df3 = pd.concat([df1, df2])
# print(df3)


# df = pd.DataFrame(
# {'a':[1,2,3,4,5,6,7,8,9],
# 'b':[1,1,1,2,2,2,3,3,3],
# 'c':[9,8,7,8,9,8,7,6,5]})
# df.index = df['a']
# df[['b', 'c']].plot()
# plt.show()

# df = pd.DataFrame(
# {'a':[1,2,3,4,5,6,7,8,9],
# 'b':[1,5,2,6,3,7,4,8,5]})
# df.plot.barh()
# df.plot.bar()
# plt.show()

# import random
# x, y = [], []
# for _ in range(10):
#     x.append(random.random())
#     y.append(random.random())
#     df = pd.DataFrame({'x':x, 'y':y})
# df.plot('x','y', kind = 'scatter')
# plt.show()
import math

x, y = [], []
for i in range(-10,11):
    x.append(i)
    y.append(i**4)
df = pd.DataFrame({'x':x, 'y':y})
df.index = df['x']
df.plot()
plt.show()


