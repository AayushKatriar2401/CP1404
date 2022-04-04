"""
String Formatting Examples
"""
name = "Gibson L-5 CES"
year = 1922
cost = 16035.5
# String Concentration
print("My guitar: " + name + ",first made in " + str(year))

# Using the str.format() function:
print(f"My guitar: {name}, first made in {year}")
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Grouping
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning Columns
numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:>5}".format(number))

# Enumerate Function
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))
    print(f"{year} {name} for about ${cost:0f}!")
for number in range(0, 151, 50):
    print(f"{number:3}")