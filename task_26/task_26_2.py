# Задача 26 2
# Создайте класс Pet ,используя функцию type и с методом dis, определенную
# заранее и печатающую все атрибуты класса Pet ( например, name, age).
# Функциюdis для метода Pet.dis определите заранее.
# Подсказка:
def dis(self):
    print(self.__dict__)

Pet = type('Pet', (), {'dis': dis})
newPet = Pet()
newPet.name = 'Vasya'
newPet.age = 2
newPet.dis()

