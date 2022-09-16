class DessertItem():
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
    def __init__(self, name, price=float, weight=float):
        super().__init__(name)
        self.price = price
        self.weight = weight

    def getters(self):
        return self.price, self.weight

    def setters(self, price, weight):
        self.price = price
        self.weight = weight

    def calculate_cost(self):
        return super().calculate_cost()


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

    def calculate_cost(self):
        return super().calculate_cost()


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

    def calculate_cost(self):
        return super().calculate_cost()


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

    def calculate_cost(self):
        return super().calculate_cost() + self.topping_price


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


def main():
    order = Order()
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", 3, .69, "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))
    order.add(IceCream("Chocolate", 3, .99))
    order.add(Cookie("Chocolate Chip", 3, 3.99))
    for item in order.getOrderList():
        print(
            f"{item.name}: ${item.calculate_cost():.2f} [Tax:{item.calculate_tax():.2f}]")
    print(
        f"Order Subtotals: ${order.order_cost():.2f} [Tax:{order.order_tax():.2f}]")
    print(f"Order Total: ${order.order_cost() + order.order_tax():.2f}")
    print(f"Total items in the order: {order.itemCount()}")


if __name__ == "__main__":
    main()
