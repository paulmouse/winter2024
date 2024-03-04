# Человек регулярно
# приходит в кафе выпить чашку кофе, выбирая
# разные варианты кофе, иногда с пирожным, выбирая, что есть в
# меню.
# Оплачивает иногда наличными деньгами, иногда картой.
# Разработайте классы, их атрибуты, свойства и методы.
# Может быть какую
# то отчетность.

class Client:
    def __init__(self, name):
        self.card = 1000
        self.cash = 1000
    def __str__(self):
        return str(self.__dict__.items())
    def buySomething(self, other, money, payType):
        self.payType = payType
        self.money = money
        if self.payType == 'card' and self.card >= self.money:
        # if self.payType == 'card':
            other.balance += money
            self.card -= money
            print(f'ok pay with card successful! balance {self.card}')
        elif self.payType == 'cash' and self.cash >= self.money:
        # if self.payType == 'cash' :
            other.balance += money
            self.cash -= money
            print(f'ok pay with cash successful! balance {self.cash}')
        else:
            print(f'payment with {self.money} from {self.payType} unsuccessful! no avalible balance!')
class Cafe:
    def __init__(self):
        self.menu = {'Coffe': 100, 'Cake': 120, 'Pie': 150, 'Tea': 70}
        self.balance = 0

    def showMenu(self):
        return self.menu

    def checkBalance(self):
        return f'cafe balance: {self.balance}'


client1 = Client('Вася')
print(client1)

cafe1 = Cafe()
print(cafe1.showMenu())

client1.buySomething(cafe1, 240, 'card')
client1.buySomething(cafe1, 240, 'cash')
client1.buySomething(cafe1, 800, 'cash')
print(client1)
print(cafe1.checkBalance())
