# from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLineEdit
# from PyQt6.QtCore import QSize, Qt
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         self.setWindowTitle("My App")
#         widget = QLineEdit()
#         widget.setMaxLength(10)
#         widget.setPlaceholderText("Enter your text")
#         # widget.setReadOnly(True)
#         widget.returnPressed.connect(self.return_pressed)
#         widget.selectionChanged.connect(self.selection_changed)
#         widget.textChanged.connect(self.text_changed)
#         widget.textEdited.connect(self.text_edited)
#         self.setCentralWidget(widget)
#
#     def return_pressed(self):
#         print("Return pressed!")
#
#     def selection_changed(self):
#         print("Selection changed")
#
#     def text_changed(self, s):
#         print("Text changed...")
#         print(s)
#
#     def text_edited(self, s):
#         print("Text edited...")
#         print(s)
# app = QApplication([]) # приложение
# window = MainWindow()
# window.show() ##окно по умолчанию скрыто.
# app.exec() # запускаем цикл событий, которые обрабатывает приложение


# class Person:
#     def __init__(self,name):
#         self.__age = 1
#         self.__name = name
#     def setAge(self, age):
#         if 1<age<120:
#             self.__age = age
#     def getAge(self):
#         return self.__age
# tom = Person('Tom')
# tom.setAge(25)
# print(tom.getAge())


class Cat:
    def __init__(self, name, age):
        self.__name = name # имя кошки
        self.__age = age
    @property # геттер свойства name
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age
    @age.getter
    def age(self):
        return self.__age

    @name.setter
    def name(self, name1): # сеттер свойства name
        if name1.istitle():
            self.__name = name1
        else:
            print('Некорректный формат имени!')
    @age.setter
    def age(self, other_age): # сеттер свойства name
        self.__age = other_age
        # if 1 < other_age < 20:
        #     self.__age = other_age
        # else:
        #     self.__age = self.__age
        #     print('Некорректный формат имени!')
    @age.deleter
    def age(self): # делитер свойства name
        del self.__age
    @name.deleter
    def name(self): # делитер свойства name
        del self.__name

c = Cat('Мurka', 10)
print(c.name)
# c.name = 'crka'
print(c.name)
c.age(33)
print(c.age)

# class Cat:
#     def __init__(self, name, age):
#         self.name = name # имя кошки
#         self.age = age
#
#     # def __getattribute__(self, item):
#     #     # if item in range(10):
#     #     #     return self.name.upper()
#     #     return item.upper()
#
#     def __setattr__(self, name, value):
#         self.__dict__[name] = value
#         print(self.__dict__)
#
#     def __delattr__(self, item):
#         self.age +=1
#         print(self.__dict__)
#     # def __getattr__(self, attr):
#     #     if attr == 'color':
#     #         return "Black"
#     #     elif attr == 'weight':
#     #         return 10
# c = Cat('Мurka', 10)
# # print(c.color, c.weight, c.name)
# c.color = 'White'
# del c.color


# class Foo():
#     bar = True

# Foo = type('Foo', (), {'bar':True})# имя, от кого наследуется, и словарь

# class Foo():
#     bar = True
# def echoBar(self):
#     print(self.bar)
#
# FooChild = type('FooChild',(Foo,), {'echoBar' : echoBar})
# my_Foo = FooChild()
#
# print(my_Foo)


# def __init__(self, name):
#     self.name = name
#
# def show(self):
#     print(self.age, self.name)
#     # return self.age
#
# Person = type('Person', (), {'age':50, 'show':show, '__init__':__init__})
#
# p = Person('Petr')
# p.show()

