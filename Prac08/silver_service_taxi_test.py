"""
CP1404

SilverServiceTaxi class test
"""

from Prac08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverService class."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
    