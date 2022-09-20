import packaging

# set the superclass packaging type within the constructor;
# the default value for each respective type is as follows:
#Candy: packaging = "Bag"
#Cookie: packaging = "Box"
#IceCream: packaging = "Bowl"
#Sundae: packaging = "Boat"


class DessertItem():
    def __init__(self, name, price, packaging):
        self._name = name
        self._price = price
        self._packaging = packaging

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def packaging(self):
        return self._packaging

    @packaging.setter
    def packaging(self, value):
        self._packaging = value

    def __str__(self):
        return "{} ${:.2f} {}".format(self.name, self.price, self.packaging)

    def __str__(self):
        return "{} ${:.2f} {}".format(self.name, self.price, self.packaging)

    def __str__(self):
        return "{} ${:.2f} {}".format(self.name, self.price, self.packaging)

    def __str__(self):
        return "{} ${:.2f}".format(self.name, self.price)

    def getters(self):
        return "{} ${:.2f} {}".format(self.name, self.price, self.packaging)

    def __init__(self, name):
        self.name = name

    def getters(self):
        return self.name

    def setters(self, name):
        self.name = name

    def get_cost(self):
        return self.price

    def tax_percent(self):
        return 7.25

    def calculate_cost(self):
        return self.get_cost() + self.get_cost() * self.tax_percent() / 100

    def calculate_tax(self):
        return self.get_cost() * self.tax_percent() / 100


class Candy(DessertItem):
    def __init__(self, name, price=float, weight=float, packaging="Bag", ):
        super().__init__(name)
        self.price = price
        self.weight = weight
        self.packaging = packaging

    def getters(self):
        return self.price, self.weight

    def setters(self, price, weight):
        self.price = price
        self.weight = weight

    def calculate_cost(self):
        return super().calculate_cost()

    def __str__(self):
        return f"{self.name} ({self.packaging})\n\t{self.weight}lbs @ ${self.price:.2f}/lb: ${self.calculate_cost():.2f} [Tax: ${self.calculate_tax():.2f}]"


class Cookie(DessertItem):
    def __init__(self, name, price=float, number=int, packaging="Box"):
        super().__init__(name)
        self.price = price
        self.number = number
        self.packaging = packaging

    def getters(self):
        return self.price, self.number

    def setters(self, price, number):
        self.price = price
        self.number = number

    def calculate_cost(self):
        return super().calculate_cost()

    def __str__(self):
        return f"{self.name} cookies ({self.packaging})\n\t{self.number} cookies @ ${self.price:.2f} dozen: ${self.calculate_cost():.2f} [Tax: ${self.calculate_tax():.2f}]"


class IceCream(DessertItem):
    def __init__(self, name, price=float, scoop=int, packaging="Bowl"):
        super().__init__(name)
        self.price = price
        self.scoop = scoop
        self.packaging = packaging

    def getters(self):
        return self.price, self.scoop, self.topping, self.topping_price

    def setters(self, price, flavor):
        self.price = price
        self.flavor = flavor

    def calculate_cost(self):
        return super().calculate_cost()

    def __str__(self):
        return f"{self.name} Ice Cream ({self.packaging})\n\t{self.scoop} scoops @ ${self.price:.2f}/scoop: ${self.calculate_cost():.2f} [Tax: ${self.calculate_tax():.2f}]"


class Sundae(IceCream):
    def __init__(self, name, price, scoop, topping=str, topping_price=float, packaging="Boat"):
        super().__init__(name, price, scoop)
        self.topping = topping
        self.topping_price = topping_price
        self.packaging = packaging

    def getters(self):
        return self.topping, self.topping_price

    def setters(self, topping, topping_price):
        self.topping = topping
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price

    def __str__(self):
        return f"{self.name} Sundae ({self.packaging})\n\t{self.scoop} scoops @ ${self.price:.2f}/scoop\n {self.topping} topping @ ${self.topping_price:.2f}: ${self.calculate_cost():.2f} [Tax: ${self.calculate_tax():.2f}]"


class Order():
    def __init__(self):
        self.order = []

    def getOrderList(self):
        return self.order

    def add(self, item):
        self.order.append(item)

    def itemCount(self):
        return len(self.order)

    def order_cost(self):
        cost = 0
        for item in self.order:
            cost += item.calculate_cost()
        return cost

    def order_tax(self):
        tax = 0
        for item in self.order:
            tax += item.calculate_tax()
        return tax

    def __str__(self):
        return f"Total items in the order: {self.itemCount()}\nOrder Subtotals: ${self.order_cost():.2f} [Tax: ${self.order_tax():.2f}]\nTotal: ${self.order_cost() + self.order_tax():.2f}"


def main_menu():
    order = Order()
    while True:
        # print("Welcome to the Dessert Shoppe")
        # print("1. Add an item to the order")
        # print("2. Remove an item from the order")
        # print("3. View the order")
        # print("4. Pay for the order")
        # choice = int(input("Enter a choice: "))
        # if choice == 1:
        print("1. Add a Candy")
        print("2. Add a Cookie")
        print("3. Add a Ice Cream")
        print("4. Add a Sundae")
        print("What would you like to add to the order? (1-4, Enter for done): ")
        choice = input("Enter a choice: ")
        if choice == ("1"):
            name = input("Enter a name: ")
            weight = float(input("Enter a weight: "))
            price = float(input("Enter a price: "))
            order.add(Candy(name, price, weight))
        elif choice == ("2"):
            name = input("Enter a name: ")
            number = int(input("Enter a number: "))
            price = float(input("Enter a price: "))
            order.add(Cookie(name, price, number))
        elif choice == ("3"):
            name = input("Enter a name: ")
            scoop = int(input("Enter a scoop: "))
            price = float(input("Enter a price: "))
            order.add(IceCream(name, price, scoop))
        elif choice == ("4"):
            name = input("Enter a name: ")
            scoop = int(input("Enter a scoop: "))
            price = float(input("Enter a price: "))
            topping = input("Enter a topping: ")
            topping_price = float(input("Enter a topping price: "))
            order.add(Sundae(name, price, scoop, topping, topping_price))
        elif choice == "":
            break
        else:
            break
    return order
    #     elif choice == 2:
    #         print("1. Remove a Candy")
    #         print("2. Remove a Cookie")
    #         print("3. Remove a Ice Cream")
    #         print("4. Remove a Sundae")
    #         choice = int(input("Enter a choice: "))
    #         if choice == 1:
    #             name = input("Enter a name: ")
    #             price = float(input("Enter a price: "))
    #             weight = float(input("Enter a weight: "))
    #             order.remove(Candy(name, price, weight))
    #         elif choice == 2:
    #             name = input("Enter a name: ")
    #             price = float(input("Enter a price: "))
    #             number = int(input("Enter a number: "))
    #             order.remove(Cookie(name, price, number))
    #         elif choice == 3:
    #             name = input("Enter a name: ")
    #             price = float(input("Enter a price: "))
    #             scoop = int(input("Enter a scoop: "))
    #             order.remove(IceCream(name, price, scoop))
    #         elif choice == 4:
    #             name = input("Enter a name: ")
    #             price = float(input("Enter a price: "))
    #             scoop = int(input("Enter a scoop: "))
    #             topping = input("Enter a topping: ")
    #             topping_price = float(input("Enter a topping price: "))
    #             order.remove(
    #                 Sundae(name, price, scoop, topping, topping_price))
    #     elif choice == 3:
    #         for item in order.getOrderList():
    #             print(item.getters())
    #     elif choice == 4:
    #         break
    # return order
