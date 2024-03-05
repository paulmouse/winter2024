import numpy as np

def findWay(arr):
    rows = len(arr)
    cols = len(arr[0])
    xe = cols - 1
    ye = rows - 1
    way = []
    sum = 0
    # print(arr[xs+1, ys])
    # print(arr[xs, ys+1])
    # print('s', start)
    while xe > 0 or ye > 0:
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
    return  sum + arr[0, 0]

arr = np.array([[3, 5, 1], [1, 4, 5], [3, 5, 1]])
testWay = findWay(arr)
# print(arr)
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






