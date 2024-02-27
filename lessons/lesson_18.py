#print(11 > 0 is True) # chained comparisons
# print(0 < 0 == 0)
# print(1 in range(2) == True)
# print( (11 > 0) is True)
# print((0 < 0) == 0)
# print((1 in range(2)) == True)

# Инкапсуляция, Наследование, Полиморфизм, Абстракция
# Полиморфизм: в разных объектах одна и та же операция может выполнять различные функции
# Инкапсуляция: можно скрыть ненужные внутренние подробности работы объекта от окружающего мира
# Наследование: можно создавать специализированные классы на основе базовых
# Абстракция: создавать интерфейсы и классы, которые определяют только те свойства и методы,
# которые необходимы для выполнения определенной задачи.

# class Figure:
#     lst = []
#     def __init__(self, perimeter, color, name):
#         self.perimeter = perimeter
#         self.color = color
#         self.name = name
#         # Figure.lst.append(self)
#         # for i in Figure.lst:
#         #     print(i.name,i.color, i.perimeter)
#         # print()
#     def getPerimeter(self):
#         return self.perimeter
#         # pass
#     def show(self):
#         print('Figure', self.color, self.perimeter)
#
# class Triangle(Figure):
#     def __int__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.calcPerimeter
#
#     def calcPerimeter(self):
#         self.perimeter = self.a + self.b + self.c
#
# # class Rectangle(Figure):
# #     def __int__(self,a,b):
# #         self.a = a
# #         self.b = b
# #         self.calcPerimeter
# #     def calcPerimeter(self):
# #         self.perimeter = (self.a + self.b)*2
#
# tri = Triangle(7,8,0)
# print(tri.getPerimeter())
# ccc = Rectangle(1,3,5)
# print('qqq',ccc.getPerimeter())
# deg = Figure(234, 'Blue', 'синий')
# gfr = Figure(444, 'Black', 'черный')

# print(abc.__class__)
# print(dir(abc))


# Класс
# Класс универсальный , комплексный тип данных состоящий из
# тематически единого набора « полей » ( переменных более элементарных
# типов ) и « методов » ( функций для работы с этими полями), то есть он
# является моделью информационной сущности с внутренним и внешним
# интерфейсами для оперирования своим содержимым значениями полей

# В частности , в классах широко используются специальные блоки из одного
# или чаще двух спаренных методов , отвечающих за элементарные операции
# с определённым полем интерфейс присваивания и считывания значения),
# которые имитируют непосредственный доступ к полю

# class Tree(object):
#     def __init__(self, kind, height):
#         self.kind = kind
#         self.age = 0
#         self.height = height
#     def grow(self):
#         self.age += 1
#
#
# class FruitTree(Tree):
#     def __init__(self, kind, height):
#         super().__init__(kind, height)
#     def giveFruit(self):
#         print(f'Collectrd 20 kg {self.kind}')
#
# t1 = FruitTree('apple', 0.7)
# print(t1.age, t1.kind)
# t1.grow()
# print(t1.age, t1.kind)
# t1.giveFruit()
#
# t2 = FruitTree('orange', 1.6)
# t2.giveFruit()
#
# t3 = Tree('oak', 12)
# t3.giveFruit()

# class Horse:
#     isHorse = True # атрибут класса
# class Donkey:
#     isDonkey = True # атрибут класса
# class Mule (Horse,Donkey):
#     pass
# mule = Mule()
# print(mule.isHorse) # True
# print(mule.isDonkey) # True

# Полиморфизм
# class X(str):
#     def __init__(self,s):
#         self.s = s
#     def __add__(self, other):
#         return other.s.upper() + self.s
# class Y(int):
#     def __init__(self,s):
#         self.s = s
#     def __add__(self, other):
#         return self.s * other.s
#     def __mul__(self, other):
#         return self.s + other.s
# # x = X('aaa')
# # y = X('bbb')
# # print(x + y)
#
# y = Y(11)
# x = Y(22)
# print(x + y)
# print(x * y)
#
# print(y + y)

# class Car:
#     def __init__(self, model, color, VIN):
#         self.model = model
#         self.color = color
#         self.VIN = VIN
#     # def __str__(self):
#     #     return f'Model {self.model}, Color {self.color}, VIN {self.VIN}'
#     def __repr__(self):
#         return f'Model {self.model}, Color {self.color}, VIN {self.VIN}'
#
# car = Car('mers', 'Black', 'vvvv22223333')
# # repr(car)
# print(car)


# class SomeClass:
#     def __init__(self):
#         self.__param = 43
#     def getParam(self):
#         return self.__param
# sc = SomeClass()
# print(sc.getParam())
# print(sc._SomeClass__param)



class Person:
    def __init__(self, name):
        self.__name = name
        self.__age = 1
    def setAge(self, age):
        if 1 < age < 100:
            self.__age = age
        else:
            print('Возраст не допустим')
    def __str__(self):
        s = ''
        for k, v in self.__dict__.items():
            ', '.join((str(k)+":"+str(v)))
        return  s


man = Person('Abc')
man.setAge(15)
print(man._Person__age)
print(man.__dict__)
print(man)
