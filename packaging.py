# Specify two methods that define an abstract property packaging using the property decorator as described in the Python docs ABC module
# make the setter an abstract method

from abc import ABC, abstractmethod

# implement the __subclasshook__ magic method to be able to test whether a class is a subclass of Packaging.


class Packaging(ABC):
    @property
    @abstractmethod
    def packaging(self):
        pass

    @packaging.setter
    @abstractmethod
    def packaging(self, value):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is Packaging:
            if any("__packaging__" in B.__dict__ for B in subclass.__mro__):
                return True
        return NotImplemented
