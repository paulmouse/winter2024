class Person:
    def __init__(self, name1, name2, name3): #args
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    def __str__(self):
        full = f'{self.name1}{self.name2}{self.name3}'
        return full[::-1]
        # return ''.join(self.name1,self.name2,self.name2)


p = Person('Иванов', 'Исаак','Абдурахманович')
print(p)