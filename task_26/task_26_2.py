
def dis(self):
    print(self.__dict__)

Pet = type('Pet', (), {'dis': dis})
newPet = Pet()
newPet.name = 'Vasya'
newPet.age = 2
newPet.dis()

