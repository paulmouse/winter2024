# Задача 8-3
# Дан список слов. Отсортируйте его по количеству уникальных букв в каждом слове в обратном порядке.
# Например:
# ['abab’,‘xx’, 'aaaaaaa', 'abcbab']
# Результат:
# ['abcbab’, 'abab’, 'aaaaaaa’,'xx']
# Если число уникальных букв одинаково, то порядок алфавитный.


words = ['abab','xxx','ccc','bbb','fgdgfhf']

# def sortW(w):
#     return (len(set(x)) for x in w)

# sortedWords = sorted(words, key=lambda x: (len(set(x)), x), reverse=True)
sortedWords = sorted(words, key=lambda x: (-len(set(x)), x), reverse=False)

# sv = sorted(words, key=sortW)
#
# print(sv)

print(sortedWords)