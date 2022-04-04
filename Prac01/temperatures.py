"""
Temprature Conversion
"""
Main_Menu = """C - Convert Celcius to Fahrenheit
F - Convert Fahrenheit to Celcius
Q - Quit Program"""
print(Main_Menu)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celcius = float(input("Temp in Celcius: "))
        fahrenheit = celcius * 9.0 / 5 + 32
        print("Result: {:2f} F".format(fahrenheit))

    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celcius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:2f} C".format(celcius))

    else:
        print("Invalid!")
        print(Main_Menu)

choice = input(">>> ").upper()
print("Program Completed! Thank You.")