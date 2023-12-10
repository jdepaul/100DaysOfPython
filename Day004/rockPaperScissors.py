import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0, 2)

if user_choice == 0:
  print(rock)
  if computer_choice == 0:
    print(rock)
    print("You tie")
  elif computer_choice == 1:
    print(paper)
    print("Paper covers rock. You lose.")
  else:
    print(scissors)
    print("Scissors blunts rock. You win.")
elif user_choice == 1:
  print(paper)
  if computer_choice == 0:
    print(rock)
    print("Paper covers rock. You win.")
  elif computer_choice == 1:
    print(paper)
    print("You tie")
  else:
    print(scissors)
    print("Scissors cuts paper. You lose.")
else:
  print(scissors)
  if computer_choice == 0:
    print(rock)
    print("Rock blunts scissors. You lose.")
  elif computer_choice == 1:
    print(paper)
    print("Scissors cuts paper. You win.")
  else:
    print(scissors)
    print("You tie.")


