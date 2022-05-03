"""
CP1404

Client Code for Car Class.
"""

from Prac06.car import Car


def main():
    """Demo test to show how to use class."""
    my_car = Car("My car", 180)
    my_car.drive(30)
    print("fuel = ", my_car.fuel)
    print("odo = ", my_car.odometer)
    print(my_car)

    print(f"Car {my_car.fuel}, {my_car.odometer}")
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)


main()