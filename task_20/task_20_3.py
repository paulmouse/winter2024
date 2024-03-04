# Задача 20 3
# Создайте класс, экземпляр которого генерирует бесконечную
# циклическую последовательность из чисел и больших латинский букв.
# 1, A, 2, B, 3, C, .., X, 25, Y, 26, Z,1,A,2,B,3,C,..,X,25,Y,26,Z
# , 1,

class InfiniteCycleSequence:
    def __init__(self):
        self.counter = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.counter % 2 == 0 and self.counter < 27 * 2:
            next_item = chr(65 + self.counter // 2 - 1)
        elif self.counter > 26 * 2:
             self.counter = 0
             next_item = chr(65 + self.counter // 2 - 1)
        else:
            next_item = self.counter // 2 + 1
        self.counter += 1
        return next_item

s = InfiniteCycleSequence()

for _ in range(1000):
    print(next(s), end=',')



 # Вариант который не заработал
# import string
# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#         self.abc = string.ascii_uppercase
#         self.letterCount = 27
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             for u in self.abc:
#                 print(f'{self.counter} {u}')
#             return self.counter
#         else:
#             raise StopIteration
# s_iter1 = SimpleIterator(27)
# # print(next(s_iter1))
# # print(next(s_iter1))
# # print(next(s_iter1))
#
# for i in s_iter1:
#     print(i)
#
# # alphabet = [chr(i) for i in range(65, 91)]
# # print(alphabet)