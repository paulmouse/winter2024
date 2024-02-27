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
    def __init__(self, color='Blue', square=0):
        self.color = color
        self.square = square
    def colorSet(self, color):  #setColor
        self.color = color
    def colorAsk(self):         #getColor
        print(self.color)
        #return self.color  # так правильнее и аккуратнее
    def squareSet(self, square):
        self.square = square
    def squareAsk(self):
        print(self.square)


retangle = Shape('Red', 234)
triangle = Shape()
triangle.colorAsk()
triangle.squareAsk()
retangle.colorAsk()
retangle.colorSet('Green')
retangle.colorAsk()
retangle.squareAsk()
retangle.squareSet(55)
retangle.squareAsk()

