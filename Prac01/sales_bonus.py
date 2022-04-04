"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1000, the user gets a 10% bonus.
If sales are $1000 or over, the bonus is 15%
"""
sales = float(input("Enter Sales: $"))
if sales < 1000:
    Sales_Bonus = sales * (10 / 100)
else:
    Sales_Bonus = sales * (15 / 100)
    print(f"The Bonus You will receive is {Sales_Bonus}, congratulations!")
