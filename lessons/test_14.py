lst = [1, 2, 3, 4, 5, 6]
res = lst * 1
summa = 0
for i, j in enumerate(lst):
    summa += lst[i]
    res[i] = summa

print(res)