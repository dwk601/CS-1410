import time
import sys


class CashBox(object):
    def __init__(self):
        self.credit = 0
        self.totalReceived = 0
        #self.price = 35

    def deposit(self, amount):
        self.credit = amount + self.credit
        self.totalReceived = amount + self.totalReceived
        print("Depositing {0} cents. You have {1} cents credit.".format(
            amount, self.credit))
        # print(type(self.credit))
        return self.credit

    def returnCoins(self):
        print("Returning ", self.credit/100, " dollars.")
        self.totalReceived = 0

    def haveYou(self, name, price, recipe):
        return self.credit >= price

    def deduct(self, amount):
        pass

    def totalCoins(self):
        return self.totalReceived


class CoffeeMachine(object):

    def __init__(self):
        self.cashBox = CashBox()
        self.credit = CashBox.__init__
        self.selector = self.cashBox

    def oneAction(self):

        while True:
            command = input("""
            ______________________________________________________
            PRODUCT LIST: all 35 cents, except bouillon (25 cents)
            1=black, 2=white, 3=sweet, 4=sweet & white, 5=bouillon      
            Sample Commands: insert 25, select 1, cancel, quit.
            Your command: 
            """)
            words = command.lower().split()
            if 'select' in words:
                Selector.select(self, int(words[1]))
            elif 'insert' in words:
                coinsAllowed = [5, 10, 25, 50]
                if int(words[1]) in coinsAllowed:
                    self.cashBox.deposit(int(words[1]))
                else:
                    print(
                        """We only take half-dollars, quarters, dimes, and nickels.""")
            elif 'cancel' in words:
                print("Cancelling transaction. Returning to main menu: ")
                self.cashBox.returnCoins()
            elif 'quit' in words:
                break
            else:
                print("Invalid command.")

    def totalCash(self):
        return self.cashBox.totalReceived


class Product(object):

    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        for item in self.recipe:
            print("dispensing", item)
            time.sleep(0.5)
        print("Enjoy your", self.name)
        time.sleep(0.5)
        # print(self.price)


class Selector(object):

    def __init__(self):
        #self.Product = Product()
        self.cashBox = CashBox()
        self.credit = CashBox.deposit
        # self.products.append(Product.

    def select(self, choiceIndex):
        recipes = {
            1: ["Black coffee", 35, ["cup", "coffee", "water"]],
            2: ["White coffee", 35, ["cup", "coffee", "creamer", "water"]],
            3: ["Sweet coffee", 35, ["cup", "coffee", "sugar", "water"]],
            4: ["White & Sweet coffee", 35, ["cup", "coffee", "sugar", "creamer", "water"]],
            5: ["Bouillon", 25, ["cup bouillonPowder", "water"]]
        }
        if choiceIndex in range(1, len(recipes)+1):
            self.choiceIndex = choiceIndex
            self.recipe = recipes.get(choiceIndex)
            product = Product(*self.recipe)
            if self.cashBox.haveYou(*self.recipe) == True:
                #print(self.recipe,"Great selection")
                #price = CashBox.haveYou(*self.recipe)
                product.make()
                self.cashBox.haveYou = self.cashBox.haveYou - self.cashBox.deduct
                print("Returning {0} cents.".format(self.cashBox.haveYou))
            else:
                print("Sorry. Not enough money deposited.")
        else:
            print("That selection does not exist")


def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash received: ${total/100:.2f}")


if __name__ == "__main__":
    main()
