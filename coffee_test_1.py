class CashBox(object):
    def __init__(self):
        self.credit = 0
        self.totalReceived = 0.0

    def deposit(self, amount):
        self.credit = amount + self.credit
        self.totalReceived = amount + self.totalReceived
        print(self.totalReceived, self.credit)

    def returnCoins(self):
        print("Returning ", self.totalReceived, " cents.")
        self.totalReceived = 0.0

    def haveYou(self, amount):
        return self.credit >= amount

    def deduct(self, amount):
        pass

    def totalCoins(self):
        return self.totalReceived


class CoffeeMachine(object):

    def __init__(self):
        self.cashBox = CashBox()
        self.selector = self.cashBox

    def oneAction(self):

        while True:
            command = input("""
            ______________________________________________________
            PRODUCT LIST: all 35 cents, except bouillon (25 cents)
            1=black, 2=white, 3=sweet, 4=sweet & white, 5=bouillon      
            Sample Commands: insert 25, select 1. Your command: 
            """)
            words = command.lower().split()
            if 'select' in words:
                Selector.select(self, int(words[1]))
                print("Great selection!")
            elif 'insert' in words:
                coinsAllowed = [5, 10, 25, 50]
                if int(words[1]) in coinsAllowed:
                    CashBox.deposit(self, int(words[1]))
                else:
                    print("""
                    TWe only take half-dollars, quarters, dimes, and nickels.
                    """)
            elif 'cancel' in words:
                print("Cancelling transaction. Returning to main menu: ")
                CashBox.returnCoins(self)
            elif 'quit' in words:
                print("Total cash received: $", self.cashBox.totalReceived)
            else:
                print("Invalid command.")

    def totalCash(self):
        pass


class Product(object):

    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print(self.recipe)


class Selector(object):

    def __init__(self):
        self.cashBox = CashBox
        self.products = []
        # self.products.append(Product.

    def select(self, choiceIndex):
        pass


def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    #total = m.totalCash()
    #print(f"Total Cash: ${total/100:.2f}")


if __name__ == "__main__":
    main()
