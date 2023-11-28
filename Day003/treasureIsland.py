piratehead = "        ______\n"
piratehead +=    "_.-':::::::`.\n"
piratehead +=    "   \::::::::::::`.-._\n"
piratehead +=    "    \:::''   `::::`-.`.\n"
piratehead +=    "     \         `:::::`.\n"
piratehead +=    "      \          `-::::`:\n"
piratehead +=    "       \______       `:::`.\n"
piratehead +=    "       .|_.-'__`._     `:::\\\n"
piratehead +=    "      ,'`|:::|  )/`.     \:::\n"
piratehead +=    "     /. -.`--'  : /.\     ::|\n"
piratehead +=    "     `-,-'  _,'/| \|\\    |:|\n"
piratehead +=    "      ,'`::.    |/>`;'\   |:|\n"
piratehead +=    "      (_\ \:.:.:`((_));`. ;:|\n"
piratehead +=    "      \.:\ ::_:_:_`-','  `-:|\n"
piratehead +=    "       `:\\|     SSt:\n"
piratehead +=    "          )`__...---'\n"

print(piratehead)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")

if choice1.lower() == "left":
  choice2 = input("\nYou come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")
  if choice2.lower() == "wait":
    print("A boat appears to carry you to the other side.\n")
    choice3 = input("When you arrive at the island, there is a fort with three doors. Do you choose the red door, blue door or yellow door? (enter red, blue or yellow) ")
    if choice3.lower() == "red":
      print("\nYou are confronted by a small dragon. You are consumed by its flaming breath. Game over.")
    elif choice3.lower() == "blue":
      print("\nYou are ambushed by ferocious beasts. Game over.")
    else:
      print("\nYou find a fantastic treasure. You win!")
  else:
    print("\nThe creature from the black lagoon guards this water. Game over.")
else:
  print("\nYou were captured by cannibals. Game over")