"""
Menu
"""
MENU = "(H)ello (G)oodbye (Q)uit"
name = input("Enter Name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "H":
        print("Hello", name)

    elif choice == "G":
        print("Goodbye", name)

    else:
        print("Invalid Choice")

print(MENU)

choice = input(">>> ").upper()
print("Program has finished")
