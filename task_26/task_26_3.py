class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    @property
    def age(self):
        return self.__age
    @age.getter
    def age(self):
        return self.__age
    @age.setter
    def age(self, other_age):
        if 1 < other_age < 100:
            self.__age = other_age
        else:
            # self.__age = self.__age
            print('Недопустимый возраст!')
    @age.deleter
    def age(self):
        del self.__age

c = Person('Ivan', 19)
c.age = 23
print(c.age)
