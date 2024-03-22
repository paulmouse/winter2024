class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __getattr__(self, attr):
        if attr == 'total':
            return self.price * self.quantity
        # elif attr == 'name':
        #     return self.name.capitalize()

    @property
    def name(self):
        # self._name.title
        return self._name.capitalize()

    @name.setter
    def name(self, value):
        self._name = value

i = Item("элемент", 100, 2)
print(i.name)
print(i.total)