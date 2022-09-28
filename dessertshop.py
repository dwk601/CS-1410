import dessert
from tabulate import *


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
        for i in range(len(table)):
            table[i][1] = "$" + str(table[i][1])
            table[i][2] = "[Tax: $" + str(table[i][2]) + "]"
    print(tabulate(table, headers=["Item", "Cost", "Tax"]))
    # print(tabulate(table))
    print("------------------------------------------------------")
    total_table = [order, order.total_cost(), order.total_tax()]
    total_table[1] = "$" + str(total_table[1])
    total_table[2] = "[Tax: $" + str(total_table[2]) + "]"


if __name__ == "__main__":
    main()
