"""
CP1404

Unreliable Car Class Test
"""

from Prac08.unreliable_car import UnreliableCar


def main():
    """Testing the Unreliable Cars."""

    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Dodgy", 100, 9)

    for i in range(1, 12):
        print("Attempting to drive {}km".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
