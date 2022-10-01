import dessert as dessert
from tabulate import *
from payment import *


def main():
    order = dessert.main_menu()
    print("------------Receipt------------")
    # print item.__str__() on the left, item.calculate_cost() on the center,
    # and item.calculate_tax() on the right in a table format
    table = []
    for item in order.getOrderList():
        table.append(
            [item.__str__(), item.calculate_cost(), item.calculate_tax()])
        # edit the elements in the list, add "$"" to the beginning of the cost and tax
        table[-1][1] = "$" + str(table[-1][1])
        table[-1][2] = "[Tax: $" + str(table[-1][2]) + "]"
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
