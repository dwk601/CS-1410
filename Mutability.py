# Exercise 1

class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    def compared_to_earth(self):
        """Determines the size of a celestial
        body relative to Earth using diameter"""
        earth = 12756.3
        relative_size = self.diameter / earth
        return relative_size

# Exercise 2


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons


mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)


def closer_to_sun(body1, body2):
    """Returns the name of the body
    that is closest to the sun"""
    if body1.distance < body2.distance:
        return body1.name
    else:
        return body2.name

# Exercise 3


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons


def make_earth(cls):
    return CelestialBody("Earth", 12756.3, 149600000, 1)

# Exercise 4


class Library:
    """List of available books and list of books on loan"""

    def __init__(self):
        self.available = []
        self.on_loan = []


def add_books(self, books):
    """Add each book to the list of available books"""
    for book in books:
        self.available.append(book)


def borrow_book(self, book):
    """Remove book from available list and add to on loan list"""
    self.available.remove(book)
    self.on_loan.append(book)


def return_book(self, book):
    """Remove book from on loan list and add to availabe list"""
    self.on_loan.remove(book)
    self.available.append(book)


# Exercise 5

class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter",
                      "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0


def change_fare(cls, new_fare):
    """Change fare for all instances of Subway class"""
    Subway.fare = new_fare


def board(self, new_passengers):
    """Adds the number of people boarding the subway.
    Also adds to total_fares for the new passengers"""
    self.passengers += new_passengers
    self.total_fares += new_passengers * Subway.fare


def disembark(self, passengers_leaving):
    """Subtracts the number of people exiting the subway"""
    if passengers_leaving > self.passengers:
        self.passengers = 0
    else:
        self.passengers -= passengers_leaving


def advance(self):
    """Advances the subway to the next stop"""
    current_index = self.stops.index(self.current_stop)
    if self.direction == "south":
        if self.current_stop == "Kendall":
            self.current_stop = "Central"
            self.direction = "north"
        else:
            self.current_stop = self.stops[current_index + 1]
    else:
        if self.current_stop == "Alewife":
            self.current_stop = "Davis"
            self.direction = "south"
        else:
            self.current_stop = self.stops[current_index - 1]


def distance(self, desired_stop):
    """Returns the number of stops between the
    current location and the desired stop"""
    current_index = self.stops.index(self.current_stop)
    desired_index = self.stops.index(desired_stop)
    return abs(current_index - desired_index)
