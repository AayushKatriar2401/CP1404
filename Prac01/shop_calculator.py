"""
Shop Calculator
"""
final_price = 0
no_items = int(input("Number of Items: "))
while no_items < 0:
   print("Invalid Value Entered!")

no_items = int(input("Number of Items: "))
for i in range(no_items):
    value = float(input("Price of Item: "))
    final_price += value
    if final_price > 100:
        final_price *= (90 / 100)
        print(f"Total price for {no_items} is ${final_price}", sep=" ")