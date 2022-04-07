"""
Lists Warmup
"""

numbers = [3, 1, 4, 1, 5, 9, 2]

# Changing the first element of numbers to "ten"
numbers[0] = "ten"

# Changing the last element of numbers to 1
numbers[-1] = 1

# Getting all the elements from numbers except for the first two elements
print(numbers[:2])

# Checking to see if 9 is an elements in numbers
exist = numbers.count(9)
if exist > 0:
    print("9 exists in the list")
else:
    print("9 does not exist in the list")
