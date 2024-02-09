# Задача 11-1
# Каждый третий четверг каждого месяца билеты в Эрмитаж бесплатны.
# Напечатайте список дат в 2024 году, когда вход бесплатен.

import calendar
from datetime import date
for i in range(1,13):
    chet = 0
    for j in range(1, 29):
        if date(2024, i, j).weekday() == 3:# номмер дня недели
            chet += 1
            if chet == 3:# номер дня недели в месяце
                print(date(2024, i, j).strftime('%d.%m.%Y'))
                break


