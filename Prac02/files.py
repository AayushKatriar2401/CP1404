"""
Files
"""
# Quick Program 1
out_file = open("name.txt", "w")
name = input("What is your name?: ")
print(name, file=out_file)
out_file.close()

# Quick Program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Using with
with open("name.txt", "r"):
    name = in_file.read().strip()
    print(f"Your name is {name}")

# Quick Program 3
in_file = open("numbers.txt", "r")
number_01 = int(in_file.readline())
number_02 = int(in_file.readline())
in_file.close()
print(number_02 + number_01)

# 3 - Extension
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)