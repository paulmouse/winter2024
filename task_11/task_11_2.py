# Задача 11-2
#
# Дан файл с расширением .txt , содержащий в каждой строчке следующую информацию:
# номер, фамилия, имя, компания, зарплата, разделенные запятыми.
# Создайте Эксельный файл, в который перенесите эту информацию,
# предварительно отсортировав этот список по компании, по фамилии и по имени
# В конце списка добавьте строку: ИТОГО и суммарное значение всех зарплат.

import openpyxl
from openpyxl import Workbook
wb = Workbook()

wb = openpyxl.load_workbook('../files/empData.xlsx')
# print(wb.sheetnames)    # имена листов в книге
ws = wb.active


with open('../files/empData.txt','r', encoding='UTF-8') as f:
    lines = f.readlines()
    #sortLines = sorted(lines, key=lambda x: (x.split(',')[3]))
    # sortLines = sorted(lines, key=lambda x: (x.split(',')[1], x.split(',')[2], x.split(',')[3]))
    sortLines = sorted(lines, key=lambda x: (x.split(',')[3], x.split(',')[1], x.split(',')[2]))
    print(sortLines)

for i in sortLines:
    row = i.strip().split(',')
    print(row)
    #print(row[-1])
    # salSum = 0
    # salVal = int((row[-1]))
    # salSum += salVal[i]
    # print(salVal)
    # for j in row:
    #     salVal = int((row[-1]))
    #     #salSum += salVal[i]
    #     print(salSum)
    # ws.append(row)
# salSum = sum(salVal)
# print(salSum)
wb.save('../files/empData.xlsx')




    # for i in f:
    #     w = ' '.join(sorted(i.split(',') ,key = i[3]))
    #     w = ' '.join((i.split(',')))
    #     #w = ((i.split(',')))
    #     print(w)
    #         # print(w, file=f2, end='\n')
