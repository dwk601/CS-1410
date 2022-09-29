from pytest import *

# test DessertItem class
from dessert import *


class testDessertItem(object):
    def test_init(self):
        dessert = DessertItem("cookie", 1.00, "box")
        assert dessert.name == "cookie"
        assert dessert.price == 1.00
        assert dessert.packaging == "box"

    def test_getters(self):
        dessert = DessertItem("cookie", 1.00, "box")
        assert dessert.getters() == "cookie"

    def test_setters(self):
        dessert = DessertItem("cookie", 1.00, "box")
        dessert.setters("cake")
        assert dessert.name == "cake"

    def test_get_cost(self):
        dessert = DessertItem("cookie", 1.00, "box")
        assert dessert.get_cost() == 1.00

    def test_tax_percent(self):
        dessert = DessertItem("cookie", 1.00, "box")
        assert dessert.tax_percent() == 7.25

    def test_calculate_cost(self):
        dessert = DessertItem("cookie", 1.00, "box")
        assert dessert.calculate_cost() == 1.00


class testCandy(object):
    def test_init(self):
        candy = Candy("candy", 1.00, 2.00, "bag")
        assert candy.name == "candy"
        assert candy.price == 1.00
        assert candy.weight == 2.00
        assert candy.packaging == "bag"


class testCookie(object):
    def test_init(self):
        cookie = Cookie("cookie", 1.00, 2.00, "bag")
        assert cookie.name == "cookie"
        assert cookie.price == 1.00
        assert cookie.number == 2
        assert cookie.packaging == "bag"


class testIceCream(object):
    def test_init(self):
        icecream = IceCream("inecream", 1.00, "Bowl")
        assert icecream.name == "inecream"
        assert icecream.price == 1.00
        assert icecream.packaging == "Bowl"


class testSundae(object):
    def test_init(self):
        sundae = Sundae("sundae", 1.00, "Boat")
        assert sundae.name == "sundae"
        assert sundae.price == 1.00
        assert sundae.packaging == "Boat"


if __name__ == "__main__":
    testDessertItem().test_init()
    testDessertItem().test_getters()
    testDessertItem().test_setters()
    testDessertItem().test_get_cost()
    testDessertItem().test_tax_percent()
    testDessertItem().test_calculate_cost()
    testCandy().test_init()
    testCookie().test_init()
    testIceCream().test_init()
    testSundae().test_init()

    print("All tests passed!")
