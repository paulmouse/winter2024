salary = 0 # суммирующая переменная
count = 0 # количество вводов зарплат

while True:
    x = int(input())
    if x == 0:
        break
    salary += x  # суммируем ввод
    count += 1      # при каждом вводе увеличиваем количество на 1
    salaryMedian = salary / count # считаем среднее
print(salaryMedian)