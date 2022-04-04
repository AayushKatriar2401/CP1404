"""
Exceptions Demo
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    calculation = numerator / denominator

except ValueError:
    print("Numerator and Denominator are not valid!")

except ZeroDivisionError:
    print("Cannot divide by zero!")
    print("Program Finished.")
