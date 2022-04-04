"""
Loops
"""
# a) count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=" ")
    print()

# b) count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=" ")
    print()

# c) printing n-number of '*' by asking the user for the number
number_stars = int(input("Number of Stars: "))
for i in range(number_stars):
    print("*", end="")
    print()

# d) print n-lines of increasing stars
num_stars = int(input("Number of Stars: "))
for i in range(1, num_stars + 1):
    print("*" * i)
    print()
