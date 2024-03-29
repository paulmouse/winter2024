# Задание 9-3
# Произвести частотный анализ текста.
# Сосчитать с помощью словаря и функции get сколько раз встречается каждый
# символ в тексте (включая буквы, цифры и служебные символы, включая
# пробелы), не учитывая регистр.
# Отсортировать по убыванию и напечатать первые 10 символов, и их частоты.
# При равенстве частот отсортировать символы в алфавитном порядке
# Например, текст «Мама мыла раму»:
# а – 4
# м – 4
# л – 1
# И т.д.

# «Ммммммама мылаааааа раму»

strInput = (input('Input text:')).lower()
strToList = list(strInput)  # переварим строку, со всеми ее символами в лист (список)
#print(strToList)
simbolCount = {}            # пустой словарь

for i in strToList:
    if simbolCount.get(i, None): # если еще нет
        simbolCount[i] += 1
    else:
        simbolCount[i] = 1
#print(simbolCount) # оригинаальный получившийся словрь

print(sorted(simbolCount.items(), key = lambda x: (-x[1], x[0])))
# -x[1] - так как тут уже кортежи, мы сначала сортируем по элементу с индексом 1 (вторму в кортеже)
# а - в начале реверсирует сортировку
# x[0] а вторая сортировка по 0 значению (первому) в кортеже, по букве(символу).
lst = (sorted(simbolCount.items(), key = lambda x: (-x[1], x[0])))

for x in lst [:10]:
    print(x)
# [:10] до десятого, невключительно. срез
# списки
