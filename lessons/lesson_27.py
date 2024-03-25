# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __getattribute__(self, attr):
#         print(f' get attribute{attr}')
#         if attr in self.__dict__:
#             return object.__getattribute__(self, attr)
#         else:
#             raise AttributeError
#
#     def __getattr__(self, item):
#         print(f' get attr {item}')
#
#
# cat = Cat('Murca')
# print(cat.name)
# print(cat.age)

# class Anyclass:
#     def __init__(self,**kwargs):
#         for k in kwargs:
#             self.__dict__[k] = kwargs[k]
#     def __str__(self):
#         s= 'AnyClass('
#         for i in self.__dict__:
#             s += i+': '+ str(self.__dict__[i])+','
#         return s+')'
#
# ac = Anyclass(att1=1, att2=3)
# print(ac)

# xyz = type('Class1',(),{})
# x = xyz()
# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(Singleton, cls).__new__(cls)
#         return cls.instance
#
# s1 = Singleton()
# print(Singleton.instance)
# s2 = Singleton()
# print(Singleton.instance)
# print(s1 is s2) # True
# s1.x = 123
# print(s2.x) # 123


import copy
class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def __str__(self):
        return f'Person {self.name} from {self.address}'
john = Person('John', ['Nevsky', 25] )
print(john)
jane = copy.deepcopy(john)
print(jane)
jane.name = 'Jane'
print(jane)
jane.address = ['Liteiniy', 33]
print(jane)
print(john)



