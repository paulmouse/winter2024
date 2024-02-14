def palindrome_generator():
    start = 1
    while True:
        if str(start) == str(start)[::-1]:  # Проверяем, является ли число палиндромом
            yield start
        start += 1

# Создаем итератор для последовательности числовых палиндромов
palindrome_sequence = palindrome_generator()

# Выводим первые 30 числовых палиндромов
count = 0
for number in palindrome_sequence:
    print(number, end=' ')
    count += 1
    if count == 30:
        break