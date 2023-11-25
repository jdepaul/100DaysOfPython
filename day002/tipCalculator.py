print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
people = float(input("How many people in the party? "))

total = bill * 1.2
split = float(total / people)
print("You owe " , split)
