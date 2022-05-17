"""
CP1404

Unreliable Car Class
"""

from random import randint
from Prac08.car import Car


class UnreliableCar(Car):
    """An Unreliable version of a Car."""
    def __init__(self, name, fuel, reliability):
        """Initialize the Class"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the Car"""
        random_num = randint(1, 100)
        if random_num >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
