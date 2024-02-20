# import re
# st = 'but bot bit bite bottle rabbit bat batman'
# print(re.findall (r'b.t', st)) # 1
# print(re.findall (r'b\w*t', st)) # 2
# print(re.findall (r'...', st)) # 2
# print(re.findall (r'..t', st)) # 2
# print(re.findall (r'\bb\b', st)) # 2
# print(re.findall (r'b.*', st)) # 2
# print(re.findall (r'\b\w*b[aioeu]t\w* \w*\b', st)) # 2
# print(re.findall (r'\w*b[aioeu]t\w* \w* \w*', st)) # 2


# import re
#
# text = 'fizz.123.buzz.456.fizzbuzz'
# res1 = re.sub(r'\d',r'#', text)
# res2 = re.sub(r'[a-z]+',r'(*)', text)
#
# print(res1)
# print(res2)


# import re
# def fullname (x):
#     s = x.group()
#     print(x.group(), x.start(), x.end())
#     match s:
#         case 'Коля': return ' Николай ' # Коля 12 16
#         case 'Миша': return ' Михаил ' # Миша 26 30
#         case _: return '****'
#     # if s == 'Коля':
#     #     return 'Николай'
#     # elif s == 'Миша':
#     #     return 'Михаил'
#     # else:
#     #     return '****'
# text = 'Здравствуй, Коля! Привет, Миша!'
# print(re.sub(r"\b\w{4}\b", fullname, text))


# import re
# text = 'Напишите программу, которая в тексте заменит LED на Пулково, MSQ на Минск, SVO на Шереметьево, SVX на Кольцово (добавьте любимые коды)'
#
# def codes(x):
#     s = x.group()
#     match s:
#         case 'LED': return 'Пулково'
#         case 'MSQ': return 'Минск'
#         case 'SVO': return 'Шереметьево'
#         case 'SVX': return 'Кольцово'
#         case _: return '****'
#
# print(re.sub(r"\b[A-Z]{3}\b", codes, text))

# import re
# text = 'Теперик Павел Сергеевич'
# # print(re.sub(r'(\w+) (\w+)', r'\2 \1', text))
# # print(re.sub(r'(\w+) (\w+)', r'\2 \2 \1 \1', text))
# print(re.sub(r'(\w+) (\w+) (\w+)', r'\2 \3 \1', text))

# import re
# text = ('Программы на Java транслируются в байт код java, выполняемый виртуальной машиной Java (JVM) программой, '
#         'обрабатывающей байтовый код и передающей инструкции оборудованию как интерпретатор.')
# # res =re.sub(r'[Jj]ava', r'Python', text, count=2, flags=re.I)
# res =re.sub(r'Java', r'Python', text, count=5, flags=re.I)
# print(res)


# import re
# text = '123 first 234 second 4545454545 third'
# print(re.findall(r'(\d+) (\w+)', text))

# import re
# text = 'www.itmo.ru www.epam.com www.paris.net'
# print(re.findall(r'www\.(\w+)\.(?:com|by|ru)', text))

# import re
# text = 'abracadabra'
# res = re.finditer(r'[^a]', text)  #находим подстроку. ее начало, конец и соостветственно саму строку
# for i in res:
#     print(i.group(), i.start(), i.end())
# import re
#
# text = 'abracadabra'
# fnd = re.finditer(r'a', text)
# an = ''
# abr =[]
# for i in fnd:
#     an = 'A'+ str(i.start())
#     print(i.group(), i.start(), i.end())
#     abr.append(an)
#     print(abr)
#     print(str(abr))


# def func(text):
#     counter = 0
#     def change(x):
#         nonlocal counter
#         counter +=1
#         return 'A'+str(counter)
#     return re.sub(r'a', change, text)
# print(func(text))

# import re
# text = '1 + 2222 * 3 - 7 / 2'
# print(re.split( r'[\+\*\-\/]', text)) # патерн - то по какому символу нарежется строка
# print(re.split( r'[^0-9][ ]', text))


# import re
# numbers = re.compile(r'\d+')
#
# print(re.findall(numbers, 'Я живу в доме 5 в квартире 7'))
# print(numbers.findall('Прочитайте абзац 8 на странице 356'))

# import re
# x = 5
# # print(re.findall(fr'{x}', '1231231234455880340'))
# res = '|'.join(str(i) for i in range(5))
# res += '|'+'abc'
# print(re.findall(fr'{res}', '4444455555556werwerwerwerwer66sdfsdfsdf66'))

# def func(f):
#     return f
# def hello():
#     print('Привет!!!')
# hello() # просто вызов
# func(hello)() # а тут мы взывали одну функцию, с параметром в виде другой

# def speak(text):
#     def whisper (t):
#         return t.lower()
#     res = whisper(text)
#     return res
#
# print(speak('Hello WOrld'))

# def nullDeco(func):
#     return func
# def hello():
#     print('Hello World!')
#
# hello = nullDeco(hello)
# hello()

# def sampleDeco(func):
#     def wrapper():
#         print('start')
#         func()  #формальный параметр
#         print('end')
#         return  # это относится к wrapper
#     return wrapper # это относится к sampleDeco
#
# def say():
#     print('Hello World!')
#
# say = sampleDeco(say) # засовываем функцию в декоратор
# say()
# @sampleDeco   # вот так мы окончательно калечим функцию
# def goodBye():
#     print('Googbye!!!')
#
# goodBye()


# def upperCase(func):
#     def wrapper():
#         origResult = func()
#         modifyResult = origResult.upper()
#         return modifyResult
#     return wrapper
# @upperCase
# def h():
#     return 'hello'
#
# print(h())


def upperCase(func):
    def wrapper():
        origResult = func()
        #modifyResult = origResult.title()
        modifyResult = ' '.join(origResult.split()[::-1]) # поменяем порядок слов
        #modifyResult = origResult[::-1].split()
        return modifyResult
    return wrapper
@upperCase
def h():
    return 'hello world and all'

print(h())