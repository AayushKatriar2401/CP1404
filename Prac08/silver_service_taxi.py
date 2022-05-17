"""
CP1404

Silver Service Taxi class
"""

from Prac08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a Silver Service Taxi."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize a Silver Service Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        """Return a String of a Silver Service Taxi."""
        return f"{super().__str__} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the Current Fare."""
        return self.flagfall + super().get_fare()
