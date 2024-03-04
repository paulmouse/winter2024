import pandas as pd
import random
import numpy as np
df = pd.DataFrame(columns= ['Год', 'Товар', 'Шт', 'Цена'], index = range(20))
x = 0
for i in range(2001, 2006):
    for j in ['A', 'B', 'C', 'D']:
        k = [10, 20, 30, 40, 50][random.randint(0, 4)]
        m = [100, 50, 30, 20, 5][random.randint(0, 4)]
        df.iloc[x] = [i, j, k, m]
        x += 1
# print(df)
df['Итого'] = df['Шт'] * df['Цена']
print(df)

# print(df.loc[0])
# print(df[df['Цена']==20])
# print(df[df['Цена']==20 & df['Товар']=='A')

# df1 = df.set_index('Год')
# print(df1)
# df.loc[20] = [2007, 'E', 100, 2, 200]
# print(df)
# print(df.head(3))
# print(len(df['Товар'].unique()))
# print((df['Товар'].unique()))
# print((df[['Год', 'Цена']].sum()))
# print(df[['Год', 'Цена']].mean())

# df1 = df[0:2]
# df2 = df[10:12]
# df3 = pd.concat([df1,df2], ignore_index=True)
# print(df3)

# print(df[df['Товар'].isin(['A','С'])])
# print(df.sort_values(['Итого']))

# ma = df['Итого'].max()
# print(df[df['Итого'] == ma])
# print(ma)

# print(df.sort_values('Итого', ascending = False).head(3)) #1. Три самые большие сделки
# print(df.sort_values('Итого', ascending = True).head(3))
# print(df.groupby('Товар').Итого.sum())
# print(df.groupby('Товар').Итого.sum().max())
# print(df.groupby('Год').Итого.sum())
# print(df.groupby('Год').Итого.sum().max())
# print(df[df['Год'] == 2003].Итого.sum())


# print(df[1:len(df):2])
#
# mi = []
# for i in df.columns:
#     mi.append(df[i].min())
#     mi_number = min(i for i in mi if isinstance(i,(int, float)))
#     mi_str = min(i for i in mi if type(i) == str)
#     print(mi, mi_number, mi_str)


# df.to_excel('../files/test_df.xlsx')
# df.to_csv('../files/test_df.csv', index=False)


# f = open('../files/test_9.txt', 'w', encoding='utf-8')

# arr = np.array([19, 3, 9, 19, 10, 1, 4, 12, 16, 7])
# sorted_arr = np.sort(arr) # [ 1, 3, 4, 7, 9, 10, 12, 16, 19, 19]
# print(sorted_arr)