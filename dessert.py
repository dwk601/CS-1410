class DessertItem():
    def __init__(self, name):
        self.name = name

    def getters(self):
        return self.name

    def setters(self, name):
        self.name = name


class Candy(DessertItem):
    def __init__(self, name, price=float, weight=float):
        super().__init__(name)
        self.price = price
        self.weight = weight

    def getters(self):
        return self.price, self.weight

    def setters(self, price, weight):
        self.price = price
        self.weight = weight


class Cookie(DessertItem):
    def __init__(self, name, price=float, number=int):
        super().__init__(name)
        self.price = price
        self.number = number

    def getters(self):
        return self.price, self.number

    def setters(self, price, number):
        self.price = price
        self.number = number


class IceCream(DessertItem):
    def __init__(self, name, price=float, scoop=int):
        super().__init__(name)
        self.price = price
        self.scoop = scoop

    def getters(self):
        return self.price, self.scoop

    def setters(self, price, flavor):
        self.price = price
        self.flavor = flavor


class Sundae(IceCream):
    def __init__(self, name, price, scoop, topping=str, topping_price=float):
        super().__init__(name, price, scoop)
        self.topping = topping
        self.topping_price = topping_price

    def getters(self):
        return self.topping, self.topping_price

    def setters(self, topping, topping_price):
        self.topping = topping
        self.topping_price = topping_price
