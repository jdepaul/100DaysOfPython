import random

import hangman_art

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for i in range(len(chosen_word)):
    display.append("_")
print(display)

#blanks = len(chosen_word)
#print(blanks)

gameOver = False
lives = 6
win = False

while not gameOver:
    guess = input("Guess a letter: ").lower()

    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            display[i] = guess

    if "_" not in display:
        gameOver = True
        win = True

    if guess not in chosen_word:
        lives -= 1

    if lives == 0:
        gameOver = True
        win = False

    print(f"{' '.join(display)}")
    print(hangman_art.stages[lives])

if win == True:
    print("You win!")
else:
    print("Sorry, you lost")
