"""
List Exercises
"""

# 1. Numbers
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print(f"The First Number is: {numbers[0]}")
print(f"The Last Number is: {numbers[-1]}")
print(f"The Smallest Number is: {min(numbers)}")
print(f"The Largest Number is: {max(numbers)}")
print(f"The Average of the Numbers is: {sum(numbers) / len(numbers)}")

# 2. Security Checker
usernames = ['jimbo', 'gilston98', 'derekf', 'WhatSup', 'NicolEye',
             'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
             'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']
username = input("Enter Username: ")
if username in usernames:
    print("Access Granted")
else:
    print("Access Denied")
