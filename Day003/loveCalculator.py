print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?

name1_lc = name1.lower()
name2_lc = name2.lower()

n1_love = name1_lc.count("l") + name1_lc.count("o") + name1_lc.count("v") + name1_lc.count("e")
n1_true = name1_lc.count("t") + name1_lc.count("r") + name1_lc.count("u") + name1_lc.count("e")

n2_love = name2_lc.count("l") + name2_lc.count("o") + name2_lc.count("v") + name2_lc.count("e")
n2_true = name2_lc.count("t") + name2_lc.count("r") + name2_lc.count("u") + name2_lc.count("e")

num_true = n1_true + n2_true
num_love = n1_love + n2_love

score = int(str(num_true) + str(num_love))

if score <= 10 or score >= 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")


