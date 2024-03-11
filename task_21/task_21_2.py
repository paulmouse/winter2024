import numpy as np

def findWay(arr):
    rows = len(arr)
    cols = len(arr[0])
    arr = np.rot90(np.rot90(arr))
    # np.rot90(a, k=2)
    xe = rows-1
    ye = cols-1
    # xe = 0
    # ye = 0
    way = []
    sum = 0
    # print(arr)
    # print(xe, ye)
    # print(arr[xs+1, ys])
    # print(arr[xs, ys+1])
    # print('s', start)
    ####
    while xe > 0 or ye > 0:  # начало матрицы, 0,0 взято как конец выполнения цикла. Оно точно будет 0,0 всегда
        way.append((ye, xe))
        sum += arr[ye, xe]
        if ye == 0:
            xe -= 1
        elif xe == 0:
            ye -= 1
        else:
            if arr[ye - 1][xe] < arr[ye][xe - 1]:
                ye -= 1
            else:
                xe -= 1
    way.append((0, 0))
    way.reverse()
    return way, sum + arr[0, 0]
    #####

arr = np.array([[1, 3, 3], [1, 4, 3], [1, 5, 1]])
testWay = findWay(arr)
print(arr)
print(testWay)

# import pandas as pd
# df = pd.DataFrame(columns= [1, 2, 3], index = range(4))
# print(df)

# arr = np.array([[3, 5, 1], [13, 4, 5], [3, 5, 1]])
# print(arr)
# rows = len(arr)
# cols = len(arr[0])
# xs = 0
# ys = 0
# xe = cols-1
# ye = rows-1
# plus = [1,0]
# x = arr[1,0]
# start = arr[xs,ys]
# end = arr[xe,ye]
# print(rows, cols,'s',start,'e',end)
# print(x)
# print(plus)
# start += plus
# print(start)


# t = [[1,1,1,1], [9, 1,80,1], [9,2,70,1], [1,1,1,1]]
# lent = len(t)
# vbn = float('inf')
# r = {(0,0):t[0][0]}
# def pri():
#     for i in range (lent):
#         for j in range (lent):
#         print(r.get((i,j), vbn), end = ' ')
# print()
# input('---')
# for i in range (lent):
# for j in range (lent):
# if (i, j) not in r:
# r[i,j] = t[i][j] + min(r.get((i-1, j), vbn), r.get((i, (j-1)), vbn))
# r[i,j] > t[i][j] + min(r.get((i-1, j), vbn), r.get((i, (j-1)), vbn)
# elif r[i,j] = t[i][j] + min(r.get((i-1, j), vbn), r.get((i, (j-1)), vbn))
# pri ()
# xylent 1
# way = [(x, y)]
# while x > 0 or y > 0:
# if r.get((x-1,y), vbn) <r.get((x, y-1), vbn):
# x = 1
# else:
# y = 1 way.append((x, y))
# print (way)
# input("===")
# print (way[::-1])



