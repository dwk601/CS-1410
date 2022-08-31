"""Exercise 1

    Returns:
        _type_: _description_
    """


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

        """Exercise 2
        """

    @staticmethod
    def closer_to_sun(body1, body2):
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name

        """Exercise 3
        """

        """create a factory method called make_earth
        This returns aCelestialBody object for planet Earth.
        """
    @classmethod
    def make_earth(cls):
        return CelestialBody("Earth", 12756.3, 149600000, 1)

        """Exercise 4
        """


class Library:
    """List of available books and list of books on loan"""

    def __init__(self):
        self.available = []
        self.on_loan = []

    """takes a list of book titles and adds each title
    to the list of available books"""

    def add_books(self, titles):
        for title in titles:
            self.available.append(title)

    """takes a book title and moves it
    from the available list to the list of books on loan"""

    def borrow_book(self, title):
        if title in self.available:
            self.available.remove(title)
            self.on_loan.append(title)
            return True
        else:
            return False

        """takes a book tile and moves it
        from the list of books on loan to the list of available books"""

    def return_book(self, title):
        if title in self.on_loan:
            self.on_loan.remove(title)
            self.available.append(title)
            return True
        else:
            return False

        """Exercise 5
        """


class Subway:
    fare = 2.4

    def __init__(self):
        self.stops = ["Alewife", "Davis", "Porter",
                      "Harvard", "Central", "Kendall"]
        self.current_stop = "Alewife"
        self.direction = "south"
        self.passengers = 0
        self.total_fares = 0

        """accepts a float and changes the fare for all instances of the subway class
        """
    @classmethod
    def change_fare(cls, new_fare):
        Subway.fare = new_fare

    """accepts an int that represents the number of passengers boarding the subway
        """

    def board(self, new_passengers):
        self.passengers += new_passengers
        self.total_fares += Subway.fare * new_passengers

        """accepts an int that represents the number of passengers exiting the subway
        """

    def disembark(self, passengers_leaving):
        if passengers_leaving > self.passengers:
            self.passengers =0
        else:
            self.passengers -= passengers_leaving

        """moves the subway to the next stop
        """

    def advance(self):
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

        """calculates the fare for each passenger boarding the subway and adds it to total_fares
        """
    def distance(self, desired_stop):
        current_index = self.stops.index(self.current_stop)
        desired_index = self.stops.index(desired_stop)
        return abs(current_index - desired_index)

    def calculate_fare(self):
        self.total_fares += self.passengers * self.fare
        return self.total_fares

        """Exercise 6
        """
