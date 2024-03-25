def hanoi(n, source, target, auxiliary):
    if n == 1:
        print("Переместить диск 1 с", source, "на", target)
        return 1
    count = 0
    count += hanoi(n-1, source, auxiliary, target)
    print("Переместить диск", n, "с", source, "на", target)
    count += 1
    count += hanoi(n-1, auxiliary, target, source)
    return count

# Пример использования
n = 2  # Количество дисков
source_peg = 'A'  # Исходный стержень
target_peg = 'C'  # Целевой стержень
auxiliary_peg = 'B'  # Промежуточный стержень

total_moves = hanoi(n, source_peg, target_peg, auxiliary_peg)
print("Минимальное количество перемещений:", total_moves)