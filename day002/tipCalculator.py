print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = float(input("How many people to split the bill? "))

#tip_percent = .01 * tip
total = bill * (1 + (tip/100))
split = "{:.2f}".format(round((total / people), 2))
print(f"Each person should pay: ${split}")
