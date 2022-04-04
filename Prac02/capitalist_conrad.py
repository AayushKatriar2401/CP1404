"""
Capitalist Conrad
"""
import random

Max_Increase = 0.1
Max_Decrease = 0.05
Min_Price = 0.01
Max_Price = 1000.0
Start_Price = 10.0
Output_File = "stock_output.txt"
out_file = open(Output_File, "w")
price = Start_Price
day = 0
print(f"Starting Price is: ${price:.2f}", file=out_file)
while price >= Min_Price and price <= Max_Price:
    price_change = 0
    day += 1

if random.randint(1, 2) == 1:
    price_change = random.uniform(0, Max_Increase)

else:
    price_change = random.uniform(-Max_Decrease, 0)
price *= (1 + price_change)
print(f"On day {day} price is: ${price:.2f}", file=out_file)
out_file.close()
