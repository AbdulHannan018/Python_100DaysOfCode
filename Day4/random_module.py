import random
import abdul_module

random_integer = random.randint(1, 18)
print(random_integer)

print(abdul_module.favourite_number)

random_floating_number_from_0_to_1 = random.random()  # prints a floating point number: 0.0 <= X < 1.0
print(random_floating_number_from_0_to_1)

random_floating_number_from_0_to_10 = random.random() * 10  # prints a floating point number: 0.0 <= X < 10.0
print(random_floating_number_from_0_to_10)
