# Задача 2-2

myList = [3, 5, 6, 7, 33, 56, 78, 98, 23, 0.2, 6, 88, 97]   # создаём список
minVal = sum(myList)                                        # для точки отсчёта, примем скмму элементов списка за min
# print(minVal)                                             # вывод суммы
for i in range(len(myList)):
    if myList[i] < minVal:
        minVal = myList[i]
print(minVal)