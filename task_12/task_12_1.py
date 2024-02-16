# Задача 12-1
# Создайте функцию, которая принимает на вход список X и
# возвращает в качестве результата два списка:
# Список индексов элементов равных минимальному значению
# списка X
# Список индексов элементов равных максимальному значению
# списка X
# Например:
# Ввод: X = [1, 2, 3, 4, 1, 2, 3, 4, 1, 4]
# Вывод: [0, 4, 8], [3, 7, 9]
# s = list(map(int, input().split()))
# z = [int(i) for i in input().split()]


def indexSearch(lst):
    minVal = min(lst)
    maxVal = max(lst)
    print(minVal, maxVal)
    # minI = lst.index((minVal))
    # minIndexes = [lst.index((minVal) for x in lst if x == minVal]
    # minIndexes = [x in enumerate(lst) for x in lst if x == minVal]
    minIndexes = [y for y in range(len(lst)) if lst[y] == minVal]       # чуть другое решение
    # minIndexes = [y for y, x in enumerate(lst) if x == minVal]
    # maxIndexes = [y for y, x in enumerate(lst) if x == maxVal]
    maxIndexes = [y for y in range(len(lst)) if lst[y] == maxVal]
    print(minIndexes)
    print(maxIndexes)

    # print(minI)

indexSearch([1, 2, 3, 4, 1, 2, 3, 4, 1, 4])