import random
import my_module

random_integer = random.randint(1, 10)
random_float = random.random()

print(random_integer)
print(random_float)
print(my_module.pi)

# names = names_string.split(", ")
# # The code above converts the input into an array seperating
# #each name in the input by a comma and space.
# # 🚨 Don't change the code above 👆
# selected = random.randint(0, (len(names)-1))
# print(f"{names[selected]} is going to buy the meal today!")