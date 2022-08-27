# # Exercise 1
# from re import X


# class PracticeClass:
#     pass

# # Exercise 2


# class Cat:
#     def __init__(self):
#         self.breed = "american shorthair"
#         self.color = "black"
#         self.name = "kiwi"

# # Exercise 3


# class SuperHero:
#     def __init__(self, name, secret_identity, powers):
#         self.name = name
#         self.secret_identity = secret_identity
#         self.powers = powers


# # Exercise 4

# class Observation:
#     def __init__(self, date, temperature, elevation, penguins, precipitation=0):
#         self.date = date
#         self.temperature = temperature
#         self.elevation = elevation
#         self.penguins = penguins
#         self.precipitation = precipitation


# # Exercise 5

# class BigCat:
#     genus = "panthera"

#     def __init__(self, species, common_name, habitat):
#         self.species = species
#         self.common_name = common_name
#         self.habitat = habitat


# fruits = ["apple", "banana", "cherry"]
# fruits.remove[1]
# print(fruits)

# class person:

#     # init method is called when class is called
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     # sample method to show how to use class
#     # introduce self to access class variables
#     def say_hello(self):
#         print("Hello my name is " + self.name)

#     # class method to show the object's age
#     def say_age(self):
#         print("I am " + str(self.age) + " years old")

#     # class method to show the object's occupation
#     def say_occupation(self):
#         print("I am a " + self.occupation)

#     # set method to change the object's age
#     def setAge(self, age):
#         self.age = age

#     # get method to return the object's age
#     def getAge(self):
#         return self.age


# p = person("Dongwook", 24, "student")
# p.say_hello()
# p.say_age()
# p.say_occupation()
# p.setAge(25)
# p.say_age()

# class Person(object):

#     # constructor
#     def __init__(self, name):
#         self.name = name

#     # get name
#     def getName(self):
#         return self.name

#     # check if this person is an employee
#     def isEmployee(self):
#         return False

# # Inherited or Subclass of Person


# class Employee(Person):

#     # here we return true
#     def isEmployee(self):
#         return True


# # Python program to
# # demonstrate protected members

# # Creating a base class
# class Base:
#     def __init__(self):

#         # Protected member
#         self._a = 2

# # Creating a derived class


# class Derived(Base):
#     def __init__(self):

#         # Calling constructor of
#         # Base class
#         Base.__init__(self)
#         print("Calling protected member of base class: ",
#               self._a)

#         # Modify the protected variable:
#         self._a = 3
#         print("Calling modified protected member outside class: ",
#               self._a)


# obj1 = Derived()

# obj2 = Base()

# # # Calling protected member
# # # Can be accessed but should not be done due to convention
# print("Accessing protected member of obj1: ", obj1._a)

# # # Accessing the protected variable outside
# print("Accessing protected member of obj2: ", obj2._a)


"""Introduction to Objects Exercise 2"""


class Cat:
    def __init__(self):
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"


"""Introduction to Objects Exercise 3"""


class SuperHero:
    def __init__(self, name, secret_identity, powers):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers
        
"""Introduction to Objects Exercise 4"""
class Observation:
    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.penguins = penguins
        self.precipitation = precipitation
        
"""Introduction to Objects Exercise 5"""
class BigCat:
    genus = "panthera"

    def __init__(self, species, common_name, habitat):
        self.species = species
        self.common_name = common_name
        self.habitat = habitat