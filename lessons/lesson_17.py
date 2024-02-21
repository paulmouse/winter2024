# import re
# print(re.findall(r'<.*>', '<first> <second> <third>')) # Жадный поиск
# print(re.findall(r'<.*?>', '<first> <second> <third>')) # Ленивый поиск
# print(re.findall(r'a.*a', 'abracadabra')) # Жадный поиск
# print(re.findall(r'a.*?a', 'abracadabra')) # Ленивый поиск

# import re
# text = 'first second'
# print(re.sub(r"(first) (second)", r'\2 \1',text))
# #second first

# import re
# print(re.findall(r"Isaac\d (?=Asimov)", "Isaac1 Asimov, Isaac2 other"))

#
# import re
# # Напишите функцию, которая находит все слова в тексте,
# # содержащие заданное подслово . Под подсловом будем понимать,
# # часть слова окруженное буквами.
# # Например, для текста «Косой
# # косой косил волос на осине» для
# # подслова «ос» функция должна вывести только первые три слова.
# text = 'Косой косил волос на осине'
# print(re.findall(r'\b\w+ос\w+\b', text))

# def sample_decorator(func): # определяем декоратор
#     def wrapper():
#         print('Начало функции')
#         func() # мы обертываем функцию func , не вмешиваясь
# # в ее работу
#         print('Конец функции')
#     return wrapper
# def say():
#     print('Привет Мир !!')
# say = sample_decorator(say) # декорируем функцию
# say()
# вызываем декорированную функцию

# def fu(*args ,**kwargs):
#     res = 0
#     for x in args:
#         if type(x) == int:
#             res += x
#     for x in kwargs:
#         if type(kwargs [x]) == int:
#             res +=kwargs[x]
#     return res
# print(fu(1, 2,'abc', a = 3, b ='def'))
# # print(fu('1', '2', ‘3’, x = ‘4’, y = ‘5’)) #
#
# def decorator(func):
#     def wrapper(* args,**kwargs ):
# #Что то выполняется до вызова декорируемой функции
#         value = func(*args , **kwargs)
# # Декорируется возвращаемое значение функции
# # Чтото выполняется после вызова декорируемой функции
#         return value
#     return wrapper
# #Таким образом мы можем передать аргументы для функции func

# import time
# def timer(func):
#     def wrapper(*args ,**kwargs):
#         start = time.perf_counter()
#         val = func(*args,**kwargs)
#         end =time.perf_counter()
#         work_time = end-start
#         print(f' Время выполнения {func.__name__}:{round(work_time, 4)}сек.')
#         return val
#     return wrapper
# @timer
# def test(n):
#     return sum([(i/99)**34 for i in range(n)])
# @timer
# def sleep(n):
#     time.sleep(n)
# #res1 = test(100000)
# res2 = sleep(4)
# print(f' Результат функции test = {res2}')

# def joins(func):
#     def wrapper(*args):
#         res = ''
#         for i in args:
#             res += i
#         val = func(*args)
#         return res
#     return wrapper
#
# @joins
# def aaa(*args):
#     return
# print(aaa('12','121', 'qq'))

# import time
#
# def timer(func):
#     def wrapper(*args, **kwargs):
#         with open('../files/log.txt', 'a') as f:
#             print(time.ctime(), func.__name__, 'Start', file=f)
#             #print(time.ctime(), func.__name__, 'Start')
#         val = func(*args, **kwargs)
#         with open('../files/log.txt', 'a') as f:
#             print(time.ctime(), func.__name__, 'End', file=f)
#             #print(time.ctime(), func.__name__, 'End')
#         return val
#     return wrapper
#
# @timer
# def test1():
#     time.sleep(1)
# @timer
# def test2():
#     time.sleep(2)
#
# test1()
# test2()

# class Person:
#     def __init__(self, name, money):
#         self.name = name
#         self.money = money
#     def giveMoney(self, other, x_money):
#         if self.money >= x_money:
#             other.money +=x_money
#             self.money -=x_money
#             print('ok')
#         else:
#             print('no')
#     def info(self):
#         print(f'{self.name} have {self.money}')
#     def round(self, other):
#         self.money  = (self.money + other.money) / 2
#         other.money = self.money
#
#
# a = Person('Pit', 200)
# b = Person('Nik', 300)
#
# # print(a.name, a.money)
# # print(b.name, b.money)
# # a.giveMoney(b,55)
# a.round(b)
# #b.giveMoney(a,130)
# print(a.name, a.money)
# print(b.name, b.money)
# print(a.info())

class Pet:
    def __init__(self, name, weight, hungryLevel):
        self.name = name
        self.weight = weight
        self.hungryLevel = hungryLevel
    def info(self):
        print(f'Pet name: {self.name}, Pet weight: {self.weight}, Hungry Level: {self.hungryLevel}')

    def hungry(self):
        if self.hungryLevel < 5:
            return 'Голоден'
        if self.hungryLevel > 10:
            return 'Сыт'
        else: return 'OK'
    def feed(self, eda):
        self.hungryLevel += eda
        print(self.hungry())

a = Pet('Васька', 6, 3)
b = Pet('Шарик', 5, 1)

a.info()
print(a.hungry())
a.feed(23)

a.info()






