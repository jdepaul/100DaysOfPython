#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
total_pw_chars = nr_letters + nr_symbols + nr_numbers
new_password = ""

print(total_pw_chars)

for pw_char in range(total_pw_chars):
  pw_char = random.randint(0, 2)
  if pw_char == 0:
    if nr_letters > 0:
      rand_index = random.randint(0, len(letters)-1)
      new_password += letters[rand_index]
      #simpler:
      #  new_password += random.choice(letters)
      # print(new_password)
      nr_letters -= 1
    elif nr_numbers > 0:
      rand_index = random.randint(0, len(numbers)-1)
      new_password += numbers[rand_index]
      # print(new_password)
      nr_numbers -= 1
    else:
      rand_index = random.randint(0, len(symbols)-1)
      new_password += symbols[rand_index]
      # print(new_password)
      nr_symbols -= 1
  
  elif pw_char == 1:
    if nr_numbers > 0:
      rand_index = random.randint(0, len(numbers)-1)
      new_password += numbers[rand_index]
      # print(new_password)
      nr_numbers -= 1
    elif nr_symbols > 0:
      rand_index = random.randint(0, len(symbols)-1)
      new_password += symbols[rand_index]
      # print(new_password)
      nr_symbols -= 1
    else:
      rand_index = random.randint(0, len(letters)-1)
      new_password += letters[rand_index]
      # print(new_password)
      nr_letters -= 1

  else:
    if nr_symbols > 0:
      rand_index = random.randint(0, len(symbols)-1)
      new_password += symbols[rand_index]
      # print(new_password)
      nr_symbols -= 1
    elif nr_letters > 0:
      rand_index = random.randint(0, len(letters)-1)
      new_password += letters[rand_index]
      # print(new_password)
      nr_letters -= 1
    else:
      rand_index = random.randint(0, len(numbers)-1)
      new_password += numbers[rand_index]
      # print(new_password)
      nr_numbers -= 1