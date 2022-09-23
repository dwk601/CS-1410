# Exercise 1

# import tech

# my_phone = tech.Phone('Pixel 5', 'sage', 128)
# my_laptop = tech.Laptop('MacBook Pro', 15, 256)

# print(my_phone)
# print(my_laptop)


# Exercise 2

# class Band:
#     def __init__(self, name, genre, members):
#         self.name = name
#         self.genre = genre
#         self.members = members

#     def __str__(self):
#         return f'{self.name} is a {self.genre} band.'

#     def __repr__(self):
#         return f'Band({self.name}, {self.genre}, {self.members})'


# dead = Band('The Grateful Dead', 'rock\'n roll', [
#             'Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])

# print(dead)
# print(repr(dead))

# Exercise 3

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def __str__(self):
#         return f'{self.name} is a {self.breed}.'

#     def __repr__(self):
#         return f'Dog({self.name}, {self.breed})'


# dogs = [
#     Dog('Marceline', 'German Shepherd'),
#     Dog('Cajun', 'Belgian Malinois'),
#     Dog('Daisy', 'Border Collie'),
#     Dog('Rocky', 'Golden Retriever'),
#     Dog('Bella', 'Irish Setter')
# ]

# print(dogs)

# Exercise 4

# from library import Library
# from book import Book

# library = Library()
# book1 = Book('Three Musketeers', 'Alexandre Dumas', 'fiction')
# book2 = Book('The Count of Monte Cristo', 'Alexandre Dumas', 'fiction')
# book3 = Book('Educated', 'Tara Westover', 'nonfiction')

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
# library.sort_books()

# print(library.books)
# print(library.fiction)
# print(library.nonfiction)
# print(library.search_author('Alexandre Dumas'))
# print(library.search_author('Herman Melville'))
# print(library.search_title('Educated'))
# print(library.search_title('Moby Dick'))

# Exercise 5

from shopping_cart import ShoppingCart
from item import Item

item1 = Item('milk', 1.5, 1)
item2 = Item('apple', 5, 0.75)
item3 = Item('bread', 2, 2.25)
cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

print(cart.get_total())
print(cart.get_num_items())
print(cart)
print(cart.get_items())
