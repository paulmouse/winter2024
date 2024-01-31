# Задача 7-1
# Напишите программу, которая рассчитывает НОК наименьшее общее кратное) для списка натуральных чисел.


# Эту задачу я уже решал ранее))))
# Практически не подглядывал в записи.
def nod(a, b):          # функция для поиска наибольшего делителя
    while b:            # цикл, пока существует b
        a, b = b, a % b
        #print(a)
    return a


def nok(a, b):
    #print(a * b // nod(a, b))
    return a * b // nod(a, b)

def findNok(numbers):
    result = 1
    for number in numbers:
        result = nok(result, number)
    return result

inputNumbers = [2, 4, 6]
#inputNumbers = [3, 6, 9]
#inputNumbers = [2, 22, 222]
result = findNok(inputNumbers)
print(f'NOK = {result}')