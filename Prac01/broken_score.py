"""
Fixed Program for determining Score Status
"""
score = float(input("Enter Score (out of 100: "))
if score < 0 or score > 100:
    print("The Score you have entered is invalid! Please Enter the correct score")

elif score >= 90:
    print("Excellent")

elif score >= 50:
    print("Passable")

else:
    print("Bad")
