import dessert as dessert
from tabulate import *
from payment import *


class Customer:
    next_customer_id = 0

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order_history = []
        self.customer_id = Customer.next_customer_id
        Customer.next_customer_id += 1

    def add2history(self, order):
        self.order_history.append(order)
        return self


#Add a yes/no loop so that the program asks the user if they want to start another order as soon as the current order is complete and printed.
#The user should enter “y” and then press “Enter” for yes, and anything else is no.
def main():
    order = dessert.main_menu()
    customer_name = input("What is your name? ")
    customer = Customer(customer_name)
    customer.add2history(order)
    print("Here is your order: ")
    print(order)
    print("Here is your order history: ")
    print(customer.order_history)
    print("Here is your customer ID: ")
    print(customer.customer_id)

    while True:
        print("Would you like to start another order? (y/n): ")
        choice = input("Enter a choice: ")
        if choice == ("y"):
            order = dessert.main_menu()
            customer_name = input("What is your name? ")
            customer = Customer(customer_name)
            customer.add2history(order)
            print("Here is your order: ")
            print(order)
            print("Here is your order history: ")
            print(customer.order_history)
            print("Here is your customer ID: ")
            print(customer.customer_id)
        elif choice == ("n"):
            break
        else:
            break
    print("------------Receipt------------")
    
    table = []
    for item in order.getOrderList():
        table.append(
            [item.__str__(), item.calculate_cost(), item.calculate_tax()])
        # edit the elements in the list, add "$"" to the beginning of the cost and tax
        table[-1][1] = "$" + str(table[-1][1])
        table[-1][2] = "[Tax: $" + str(table[-1][2]) + "]"
    # sort the list by cost
    table = sorted(table, key=lambda x: x[1], reverse=True)
    print(tabulate(table, headers=["Item", "Cost", "Tax"]))
    # print(tabulate(table))
    print("------------------------------------------------------")
    print("Total number of items: " + str(order.itemCount()))
    total_table = []
    total_table.append(["Subtotal", order.order_cost()])
    # round the tax to 2 decimal places
    total_table.append(["Tax", round(order.order_tax(), 2)])
    total_table.append(["Total", order.order_cost() + order.order_tax()])
    for i in range(len(total_table)):
        total_table[i][1] = "$" + str(total_table[i][1])
    print(tabulate(total_table, headers=["", ""]))
    print("Paid with " + order.pay_method)
    print("------------------------------------------------------")

    print("Thank you for shopping at the Dessert Shoppe!")


if __name__ == "__main__":
    main()
