from ast import PyCF_ALLOW_TOP_LEVEL_AWAIT
import dessert as dessert
from tabulate import *
from payment import *


#Add a module-level dictionary called customer_db: Dict[str,Customer]. The key is the customer name and the value is the Customer object.
#For simplicity we assume that customer names are unique for distinct customers.

#Changes to console application user input
    #After the order is complete (the user hits enter indicating they don’t want to add any more items), ask for the customer’s name.
    #Check to see if the customer already exists as a key in the customer_db
    #If they don’t exist in the customer_db, create a new Customer object and add it to the customer_db
    #Whether they already existed or not, get the Customer object associated with the customer name in the customer_db and add the order to the Customer object’s order history.
    #Asking for the customer name should happen AFTER you finish adding items to the order but BEFORE you ask for the payment type.

class Customer:
    next_customer_id = 0

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.order_history = []
        self.customer_id = Customer.next_customer_id
        Customer.next_customer_id += 1

    def add2history(self, order):
        self.order_history.append(order)
        return self.order_history

    def add_order_history(self, order):
        self.order_history.append(order)

    def __str__(self):
        return f"Customer Name: {self.customer_name}\nCustomer ID: {self.customer_id}\nOrder History: {self.order_history}"

    def __repr__(self):
        return f"Customer({self.customer_name})"
    
    def get_customer_name(self):
        return self.customer_name
    
    def get_customer_id(self):
        return self.customer_id
    
    



#Add a yes/no loop so that the program asks the user if they want to start another order as soon as the current order is complete and printed.
#The user should enter “y” and then press “Enter” for yes, and anything else is no.
def main():
    customer_db = {}
    order = dessert.main_menu()
    customer_name = input("What is your name? ")
    customer = Customer(customer_name)
    #set customer_id
    customer.generate_customer_id()
    customer.add2history(order)
    print(customer)

    while True:
        another_order = input("Would you like to start another order? (y/n)")
        if another_order == "y":
            order = dessert.main_menu()
            customer.add2history(order)
            print(customer)
        else:
            break
        if another_order.lower() == 'y':
            order = dessert.main_menu()
            customer.add2history(order)
            print(customer)
        else:
            break

    if customer_name not in customer_db:
        customer_db[customer_name] = customer
    else:
        customer_db[customer_name].add2history(order)

    print(customer_db[customer_name])
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
