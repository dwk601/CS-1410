# exercise 1
class Country:
    def __init__(self, name, capital, population, continent):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent


# exercise 2

class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

# exercise 3


class BankAccount():
    def __init__(self):
        self._checking = 0
        self._savings = 0

    def get_checking(self):
        return self._checking

    def set_checking(self, new_value):
        self._checking = new_value

    def get_savings(self):
        return self._savings

    def set_savings(self, new_value):
        self._savings = new_value

# 4


class Dancer:
    def __init__(self, name, nationality, style):
        self._name = name
        self._nationality = nationality
        self._style = style

    def get_name(self):
        return self._name

    def set_name(self, new_value):
        self._name = new_value

    def get_nationality(self):
        return self._nationality

    def set_nationality(self, new_value):
        self._nationality = new_value

    def get_style(self):
        return self._style

    def set_style(self, new_value):
        self._style = new_value

    name = property(get_name, set_name)
    nationality = property(get_nationality, set_nationality)
    style = property(get_style, set_style)

# 5


class Cyclist:
    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        self._name = new_value

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, new_value):
        self._nationality = new_value

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_value):
        self._nickname = new_value
