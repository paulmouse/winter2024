# Задача 15-3
# Напишите функцию, которая находит в строке все телефонные номера,
# которые удовлетворяют следующим шаблонам:
# +7(812)DDD-DDDD, +7(812)DDD-DD-DD, +7(921)DDD-DDDD, +7(921)DDD-DD-DD
# где D любая цифра
import re

inputString ='+7(812)567-7654 +7(812)333-44-55 +7(921)333-2345 +7(921)567-77-89 +7(988)123-22-55 +7(921)6578998'
#inputString ='+7(812)567-7654'
regex = r'\+7\(812\)[0-9]{3}\-[0-9]{4}|\+7\(921\)[0-9]{3}\-[0-9]{4}|\+7\(812\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}|\+7\(921\)[0-9]{3}\-[0-9]{2}\-[0-9]{2}'

print(re.findall(regex,inputString))