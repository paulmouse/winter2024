# Задача 17 - 1
# Напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим
# Напишите программу, которая устраняет повторение слов, т.е.
# результат должен быть следующим.

import re
def removeDuplicates(text):
    words = text.split()
    #print(words)
    #print(len(text))
    #woDuplicates = dict.fromkeys(words)
    #woDuplicates = set(dict.fromkeys(words))
    woDuplicates = list(dict.fromkeys(words))
    print(woDuplicates)
    return ' '.join(woDuplicates)


text = 'Напишите программу программу, которая устраняет повторение повторение слов, т.е. результат результат должен быть следующим'
result = removeDuplicates(text)
print(result)

print(re.sub(r'(\b\w+\b)\W+\1', r'\1', text, flags = re.I))

