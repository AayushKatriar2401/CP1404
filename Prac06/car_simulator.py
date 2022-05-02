"""
CP1404

Car Driving Simulator
"""

from Prac06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Car Simulator Program, demonstrating use for Car Class"""
    print("Let's drive!")
    name = input("Enter Your Car Name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(input("How many km do you wish to drive?: "))
            while distance_to_drive < 0:
                print("Distance must be >= 0")
                distance_to_drive = int(input("How many km do you wish to drive?: "))

            distance_driven = car.drive(distance_to_drive)
            print(f"The car drove {distance_driven}km", end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = int(input("How many units of fuel do you want to add to the car?: "))
            while fuel_to_add < 0:
                print("Fuel amount must be >= 0")
                fuel_to_add = int(input("How many units of fuel do you want to add to the car?: "))
            car.add_fuel(fuel_to_add)
            print(f"Added {fuel_to_add} units of fuel.")
        else:
            print("Invalid Choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print(f"\nGoodbye {car.name}'s driver.")
