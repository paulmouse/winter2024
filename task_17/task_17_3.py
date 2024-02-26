# Задание 17 3
#
# Создайте класс Shape , объекты которого имеют атрибуты Colour строка, например, «Красный», «Синий»
# Square - площадь объекта
#
# Создайте несколько методов:
# 1.Установить цвет объекта
# 2.Запросить цвет объекта и напечатать его
# 3.Задать площадь объекта
# 4.Запросить площадь объекта

class Shape:
    def __init__(self, color, square):
        self.color = color
        self.square = square
    def colorSet(self, color):
        self.color = color
    def colorAsk(self):
        print(self.color)
    def squareSet(self, square):
        self.square = square
    def squareAsk(self):
        print(self.square)


retangle = Shape('Red', 234)
retangle.colorAsk()
retangle.colorSet('Green')
retangle.colorAsk()
retangle.squareAsk()
retangle.squareSet(55)
retangle.squareAsk()

