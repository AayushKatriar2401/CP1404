"""
CP1404

Guitar
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class for storing the name of a guitar."""
    def __init__(self, name="", year=0, cost=0):
        """Initiate a Guitar"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a String Representation of a Guitar."""
        return f"{self.name} ({self.year}): ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a Guitar based on the Current Year."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the Guitar is considered vintage or not based on its age."""
        return self.get_age() >= VINTAGE_AGE

    def __1t__(self, other):
        """Less than, used for sorting the Guitars by the year they were released."""
        return self.year < other.year
