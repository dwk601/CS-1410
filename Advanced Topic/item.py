class Item:
    def __init__(self, name, price, quantity, subtotal=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = subtotal

    # Assigns the total value of the items to the subtotal attribute
    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    # Returns the subtotal attribute

    def get_subtotal(self):
        return self.subtotal

    # Returns a precise object definition; see the Expected Output section for the format
    def __repr__(self):
        return f'Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})'
