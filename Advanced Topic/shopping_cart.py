class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
        self.quantity = 0
        self.subtotal = 0

    # Add an item to the shopping cart and then calls the calculate_total method
    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    # Assigns the total value of the shopping cart to the total attribute
    def calculate_total(self):
        self.total = 0
        for item in self.items:
            item.calculate_subtotal()
            self.total += item.get_subtotal()

    # Returns the total value of the shopping cart

    def get_total(self):
        return self.total

    # Returns the number of items in the shopping cart
    def get_num_items(self):
        self.quantity = len(self.items)
        return self.quantity

    # Returns a list of all of the items in the cart
    def get_items(self):
        return self.items

    # Returns a human-readable string; see the Expected Output section for the format
    def __str__(self):
        return f'The cart has {self.get_num_items()} items for a total of ${self.get_total()}'
