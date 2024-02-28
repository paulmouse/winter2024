# def add_fruit(fruit, basket=None):
#     if basket is None:
#         basket = []
#     basket.append(fruit)
#     return basket
#
# b = add_fruit("banana")
# print(b)
# c = add_fruit("apple")
# print(c)
# d = add_fruit("orange")
# print(d)

# class SomeClass:
#     '''документация к классу'''
#     def __init__(self):
#         self.x = 12
#         self._y = 'qq'
#         self.__z = 'qq'
#     def __call__(self, *args, **kwargs):
#         '''документация к методу'''
#         return self._y * self.x
#
# xyz = SomeClass()
# print(xyz.x)
# print(xyz._y)
# # print(xyz.__z)
# print(xyz())
# print(xyz.__doc__)
# print(xyz.__call__.__doc__)

# class Test:
#     def __init__(self, name, x, y):
#         self.x = x
#         self.name = name
#         self.y = y
#     def __str__(self):
#         # print(f'Объект имеет следующие аттрибуты: {self.name}, {self.x}, {self.y}')
#         return f'Объект имеет следующие аттрибуты:{self.__dict__}'
#     def __repr__(self):
#         return str((self.__dict__))
#
# abc = Test('имя', 10, 20)
#
# print(abc.__str__())
# print(abc.__repr__())

# class Test:
#     def __init__(self, name, x, y):
#         self.x = x
#         self.name = name
#         self.y = y
#     def __eq__(self, other):
#         return self.name == other.name
#     def __ne__(self, other):
#         return self.x != other.x
#
# qqq = Test('abc', 10, 15)
# acb = Test('abc', 100, 0)
#
# print(qqq == acb)
# print(qqq == acb)

#
# class Eq:
#     def __init__(self, num):
#         self.num = num
#     def __eq__(self, other):
#         return (self.num + other.num) % 2 == 0
# x = Eq(123)
# y = Eq(5)
# u = Eq(4)
#
# print(x==y, x==u,y==u)

# class stri(str):
#     def __init__(self, s):
#         self.s = s
#     def __gt__(self, other):
#         return len(self.s) > len(other.s)
# x = stri('123')
# y = stri('5')
# u = stri('4')
#
# print(x > y)

# class Student:
#     def __init__(self, name, fives, tens,twenties):
#         self.name = name
#         self.fives = fives
#         self.tens = tens
#         self.twenties = twenties
#         self.m = 5 * self.fives + 10 * self.tens+ 20 * self.twenties
#     def __lt__(self,other):
#         return self.m < other.m
#
# s1 = Student('s1', 1,0,0)
# s2 = Student('s2', 0,1,0)
# s3 = Student('s3', 0,0,1)
#
# print(min(s1,s2,s3).name)
# print(max(s1,s2,s3).name)

# class Plus:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __add__(self, other):
#         return Plus(self.x + other.x, self.y + other.y)
#     def __str__(self):
#         return f"Plus {self.x}, {self.y}"
# a = Plus(1,2)
# b = Plus(10, 20)
# print(a + b)
# # Что напечатает?

# lst = [1,2,3,4,5]
# b = iter(lst)
# print(next(b))
# print(next(b))
# print(next(b))
# print(type(b))

# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += self.counter
#             return self.counter
#         else:
#             raise StopIteration
# s_iter1 = SimpleIterator(3)
# # print(next(s_iter1))
# # print(next(s_iter1))
# # print(next(s_iter1))
#
# for i in s_iter1:
#     print(i)


# class Factorials:
#     def __init__(self):
#         self.value = 1
#         self.index = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.value *= self.index
#         self.index += 1
#         return self.value
#
# fact = Factorials()
# for _ in range(10):
#     print(i)


# class Symm:
#     def __init__(self):
#         self.value = 1
#         self.index = 1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.value += self.index
#         self.index += 1
#         return self.value
#
# fact = Symm()
# for i in range(10):
#     print(i)

import itertools
for x in itertools.combinations([1,2,34,5],3):
    print(x, end = '')