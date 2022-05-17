"""
CP1404

Taxi Simulator
"""

from Prac08.car import Car
from Prac08.taxi import Taxi
from Prac08.silver_service_taxi import SilverServiceTaxi

MENU = "Q)uit, C)hoose taxi, D)rive"


def main():
    """Taxi Simulator Program"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's Drive!")
    print(MENU)
    menu_choice = input(">>>").upper()
    while menu_choice != "Q":
        if menu_choice == "C":
            print("Taxi's Available: ")
            display_taxis(taxis)
            taxi_choice = int(input("Choose Taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid Taxi Choice")
        elif menu_choice == "D":
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive How Far?:"))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost}")

                total_bill += trip_cost

            else:
                print("You need to choose a taxi before you can drive")

        else:
            print("Invalid Option")
        print(f"Bill to date {total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>>").upper()

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now: ")
    display_taxis(taxis)

    def display_taxis(taxis):
        """Display a numbered list of avaliable Taxis"""
        for i, taxi in enumerate(taxis):
            print(f"{i} - {taxi}")

    def run_tests():
        """Run Tests to show the workings of the Car and Taxi Class."""
        bus = Car("Datsun", 100)
        bus.drive(30)
        print("Fuel = ", bus.fuel)
        print("Odo = ", bus.odometer)
        bus.drive(55)
        print("Fuel = ", bus.fuel)
        print("Odo = ", bus.odometer)
        print(bus)

        distance = int(input("Drive How Far?: "))
        while distance > 0:
            travelled = bus.drive(distance)
            print(f"{str(bus)} travelled {travelled}")
            distance = int(input("Drive How Far? "))

        t = Taxi("Prius 1", 100)
        print(t)
        t.drive(25)
        print(t, t.get_fare())
        t.start_fare()
        t.drive(40)
        print(t, t.get_fare())

        sst = SilverServiceTaxi("Limo", 100, 2)
        print(sst, sst.get_fare())
        sst.drive(10)
        print(sst, sst.get_fare())


main()
