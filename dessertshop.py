import dessert


def main():
    order = dessert.main_menu()
    print("------------Receipt------------")
    for item in order.getOrderList():
        print(item)
    print("------------------------------------------------------")
    print(order)


if __name__ == "__main__":
    main()
