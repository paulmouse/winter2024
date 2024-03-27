def uNums(lst):
    unique = 0
    for num in lst:
        unique ^= num
    return unique

# Пример использования
lst = [2, 2, 2, 2, 7, 2, 2]

res = uNums(lst)
print(res)