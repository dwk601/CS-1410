class Product:
    '''
    Abrstraction of the drink. Responsible for knowing it's price and recipe.
    Dispenses the drink.
    '''

    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.recipe = []

    def getPrice(self):
        return int(self.price)

    def make(self):
        ingredients = ["cup", "coffee", "sugar",
                       "creamer", "water", "bouillonPowder"]
        if self.name == "black":
            self.recipe.append("\tDispensing " + ingredients[0])
            self.recipe.append("\tDispensing " + ingredients[1])
            self.recipe.append("\tDispensing " + ingredients[4])
            print('\n'.join(self.recipe))
        elif self.name == "white":
            self.recipe.append("\tDispensing " + ingredients[0])
            self.recipe.append("\tDispensing " + ingredients[1])
            self.recipe.append("\tDispensing " + ingredients[3])
            self.recipe.append("\tDispensing " + ingredients[4])
            print('\n'.join(self.recipe))
        elif self.name == "sweet":
            for i in ingredients[0:3]:
                self.recipe.append("\tDispensing " + i)
            self.recipe.append("\tDispensing " + ingredients[4])
            print('\n'.join(self.recipe))
        elif self.name == "white & sweet":
            for i in ingredients[0:5]:
                self.recipe.append("\tDispensing " + i)
            print('\n'.join(self.recipe))
        elif self.name == "bouillon":
            self.recipe.append("\tDispensing " + ingredients[0])
            self.recipe.append("\tDispensing " + ingredients[5])
            self.recipe.append("\tDispensing " + ingredients[4])
            print('\n'.join(self.recipe))
        else:
            print("Unsuccessful")
        return self.recipe
    '''
    def __str__(self):
        return '\n'.join(self.recipe)
    '''


class CoffeeMachine:
    '''
    Abstraction of the outer machine, holding all the parts. Responsible for
    constructing machine, capturing external input.
    '''

    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector()

    def cashBox(self):
        return self.cashBox

    def selector(self):
        return self.selector

    def oneAction(self):
        while True:
            print("PRODUCT LIST: all 35 cents, except bouillon (25 cents)\n1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon\nSample command: insert 25, select 1.")
            command = input("Your command: ").lower()
            if command == "insert 5":
                self.cashBox.deposit(5)
                print("Depositing 5 cents. You have {} cents credit.".format(
                    self.cashBox.credit))
            elif command == "insert 10":
                self.cashBox.deposit(10)
                print("Depositing 10 cents. You have {} cents credit.".format(
                    self.cashBox.credit))
            elif command == "insert 25":
                self.cashBox.deposit(25)
                print("Depositing 25 cents. You have {} cents credit.".format(
                    self.cashBox.credit))
            elif command == "insert 50":
                self.cashBox.deposit(50)
                print("Depositing 50 cents. You have {} cents credit.".format(
                    self.cashBox.credit))
            elif command == "select 1":
                if self.cashBox.haveYou(35) == True:
                    self.selector.select(1)
                    self.cashBox.deduct(35)
                else:
                    print("Sorry. Not enough money deposited.")
            elif command == "select 2":
                if self.cashBox.haveYou(35) == True:
                    self.selector.select(2)
                    self.cashBox.deduct(35)
                else:
                    print("Sorry. Not enough money deposited.")
            elif command == "select 3":
                if self.cashBox.haveYou(35) == True:
                    self.selector.select(3)
                    self.cashBox.deduct(35)
                else:
                    print("Sorry. Not enough money deposited.")
            elif command == "select 4":
                if self.cashBox.haveYou(35) == True:
                    self.selector.select(4)
                    self.cashBox.deduct(35)
                else:
                    print("Sorry. Not enough money deposited.")
            elif command == "select 5":
                if self.cashBox.haveYou(25) == True:
                    self.selector.select(5)
                    self.cashBox.deduct(25)
                else:
                    print("Sorry. Not enough money deposited.")
            elif command == "quit":
                break
            elif command == "cancel":
                print("Returning {} cents.".format(self.cashBox.credit))
                self.cashBox.credit = 0
            else:
                print("We only take half-dollars, quarters, dimes, and nickels.")

    def totalCash(self):
        self.totalCash = self.cashBox.credit
        return self.totalCash


class CashBox:
    '''
    Abstraction of a cashbox/change maker on a real machine.
    Responsible for accepting and tracking coins, making charges.
    '''

    def __init__(self):
        self.credit = 0

    def deposit(self, amount):
        self.amount = amount
        self.credit += amount

    def deduct(self, amount):
        self.amount = amount
        self.credit -= amount

    def haveYou(self, price):
        self.price = price
        if self.price > self.credit:
            return False
        else:
            return True


class Selector:
    '''
    Abstraction of the outer machine, holding all the parts.
    Responsible for accepting and tracking coins, making change.
    '''

    def __init__(self):
        self.cashBox = CashBox()
        self.products = ["black", "white",
                         "sweet", "white & sweet", "bouillon"]

    def cashBox(self):
        return self.cashBox

    def products(self):
        pass

    def select(self, choiceIndex):
        self.choiceIndex = choiceIndex
        if self.choiceIndex == 1:
            a = Product(self.products[0], 35)
            print("Making {}".format(self.products[0]))
            a.make()
            # self.cashBox.deduct(a.getPrice())
            # print(self.cashBox.credit)
        elif self.choiceIndex == 2:
            b = Product(self.products[1], 35)
            print("Making {}".format(self.products[1]))
            b.make()
        elif self.choiceIndex == 3:
            c = Product(self.products[2], 35)
            print("Making {}".format(self.products[2]))
            c.make()
        elif self.choiceIndex == 4:
            d = Product(self.products[3], 35)
            print("Making {}:".format(self.products[3]))
            d.make()
        elif self.choiceIndex == 5:
            e = Product(self.products[4], 25)
            print("Making {}:".format(self.products[4]))
            e.make()


def main():

    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash: ${total/100:.2f}")


if __name__ == '__main__':
    main()
