import dessert

# Call the constructor with default values

ice_cream1 = dessert.IceCream("Vanilla Ice Cream", 2.99, 3)
candy1 = dessert.Candy("Snickers", 1.99, 2.5)
cookie1 = dessert.Cookie("Chocolate Chip Cookie", 1.99, 2)
sundae1 = dessert.Sundae("Hot Fudge Sundae", 3.99, 2, "Hot Fudge", 0.99)

# print DessertItem's getters

print(ice_cream1.getters())
print(candy1.getters())
print(cookie1.getters())
print(sundae1.getters())

# modify the attributes of the objects

ice_cream1.setters(3.99, 4)
candy1.setters(2.99, 3.5)
cookie1.setters(2.99, 3)
sundae1.setters("Caramel", 1.99)

print(ice_cream1.getters())
print(candy1.getters())
print(cookie1.getters())
print(sundae1.getters())


# call the constructor with non-default values

ice_cream2 = dessert.IceCream("Chocolate Ice Cream", 3.99, 4)
candy2 = dessert.Candy("M&Ms", 2.99, 3.5)

print(ice_cream2.getters())
print(candy2.getters())
