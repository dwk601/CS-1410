from abc import abstractmethod
import functools
import packaging as packaging
from dessertshop import *
from payment import *
import dessertshop as dessertshop


@functools.total_ordering
class DessertItem():
    def __init__(self, name, price, packaging):
        self.name = name
        self.price = price
        self.packaging = packaging

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

    def getters(self):
        return self.name

    def setters(self, name):
        self.name = name

    def get_cost(self):
        return self.price

    def tax_percent(self):
        return 7.25

    def calculate_cost(self):
        return round(self.get_cost(), 2)

    def calculate_tax(self):
        return round(self.calculate_cost() * self.tax_percent() / 100, 2)
    
    def is_valid_operand(self, other):
        return (hasattr(other, "price"))
    
    def __eq__(self, other):
        if not self.is_valid_operand(other):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not self.is_valid_operand(other):
            return NotImplemented
        return self.price < other.price
    
    def is_same_as(self, other) -> bool:
        if not self.is_valid_operand(other):
            return False
        return self.price == other.price


class Candy(DessertItem):
    def __init__(self, name, price=float, weight=float, packaging="Bag", ):
        super().__init__(name, price, packaging)
        self.weight = weight

    def getters(self):
        return self.price, self.weight

    def setters(self, price, weight):
        self.price = price
        self.weight = weight

    def calculate_cost(self):
        return super().calculate_cost()*self.weight

    def __str__(self):
        return f"{self.name} ({self.packaging})\n{self.weight}lbs @ ${self.price:.2f}/lb: "
        
    def is_valid_operand(self, other):
        return (hasattr(other, "price") and hasattr(other, "weight"))
    
    def is_same_as(self, other):
        if not self.is_valid_operand(other):
            return NotImplemented
        return self.name == other.name and self.price == other.price


class Cookie(DessertItem):
    def __init__(self, name, price=float, number=int, packaging="Box"):
        super().__init__(name, price, packaging)
        self.number = number

    def getters(self):
        return self.price, self.number

    def setters(self, price, number):
        self.price = price
        self.number = number

    def calculate_cost(self):
        return super().calculate_cost()*self.number/12

    def __str__(self):
        return f"{self.name} cookies ({self.packaging})\n{self.number} cookies @ ${self.price:.2f} dozen: "
        
    def is_valid_operand(self, other):
        return (hasattr(other, "price") and hasattr(other, "number"))
    
    def is_same_as(self, other):
        if not self.is_valid_operand(other):
            return NotImplemented
        return self.name == other.name and self.price == other.price


class IceCream(DessertItem):
    def __init__(self, name, price=float, scoop=int, packaging="Bowl"):
        super().__init__(name, price, packaging)
        self.scoop = scoop

    def getters(self):
        return self.price, self.scoop, self.topping, self.topping_price

    def setters(self, price, flavor):
        self.price = price
        self.flavor = flavor

    def calculate_cost(self):
        return super().calculate_cost()*self.scoop

    def __str__(self):
        return f"{self.name} Ice Cream ({self.packaging})\n{self.scoop} scoops @ ${self.price:.2f}/scoop: "


class Sundae(IceCream):
    def __init__(self, name, price, scoop, topping=str, topping_price=float, packaging="Boat"):
        super().__init__(name, price, scoop, packaging)
        self.topping = topping
        self.topping_price = topping_price

    def getters(self):
        return self.topping, self.topping_price

    def setters(self, topping, topping_price):
        self.topping = topping
        self.topping_price = topping_price

    def calculate_cost(self):
        return super().calculate_cost()*self.scoop + self.topping_price

    def __str__(self):
        return f"{self.name} Sundae ({self.packaging})\n{self.scoop} scoops @ ${self.price:.2f}/scoop\n {self.topping} topping @ "
    


    


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

    def pay_method(self):
        return self._pay_method

    def pay_method(self, value):
        self._pay_method = value

    def __str__(self):
        return f"Total items in the order: {self.itemCount()}\nOrder Subtotals: ${self.order_cost():.2f}\nTax: ${self.order_tax():.2f}\nOrder Total: ${self.order_cost()+self.order_tax():.2f}\nPaid with {self.pay_method}"

    def order_cost_str(self):
        return f"Order Subtotals: ${self.order_cost():.2f}"

    def order_tax_str(self):
        return f"Tax: ${self.order_tax():.2f}"
    
    def total_cost(self):
        return self.order_cost()+self.order_tax()
    
    def add_item(self, item):
        self.order.append(item)

    def remove_item(self, item):
        self.order.remove(item)

    def clear(self):
        self.order = []




def main_menu():
    customer_list = []
    order = Order()
    while True:
        print("1. Add a Candy")
        print("2. Add a Cookie")
        print("3. Add a Ice Cream")
        print("4. Add a Sundae")
        print("5. Admin Module")
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
        elif choice == ("5"):
            #1. Shop Customer List
            #2. Customer Order History
            #3. Best Customer
            #4. Exit Admin Module
            print("1. Shop Customer List")
            print("2. Customer Order History")
            print("3. Best Customer")
            print("4. Exit Admin Module")
            choice = input("Enter a choice: ")
            if choice == ("1"):
                print("1. Add a Customer")
                print("2. Remove a Customer")
                print("3. Exit")
                choice = input("Enter a choice: ")
                if choice == ("1"):
                    name = input("Enter a name: ")
                    customer_list.append(Customer(name))
                elif choice == ("2"):
                    name = input("Enter a name: ")
                    customer_list.remove(Customer(name))
                elif choice == ("3"):
                    break
            elif choice == ("2"):
                print(Customer.get_order_history())
            elif choice == ("3"):
                print(Customer.get_best_customer())
            elif choice == ("4"):
                print("Exit Admin Module")
                break
            else:
                print("Invalid choice")
            
        # if user enters a blank line, go to the pay_method choice
        elif choice == "":
            print("1. Cash")
            print("2. Credit")
            print("3. Check")
            choice = input("Enter a choice: ")
            if choice == ("1"):
                order.pay_method = "Cash"
            elif choice == ("2"):
                order.pay_method = "Credit"
            elif choice == ("3"):
                order.pay_method = "Check"
            else:
                print("Invalid choice, please try again.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue
    return order
