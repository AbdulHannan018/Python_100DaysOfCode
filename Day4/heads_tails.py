import random
random_integer = random.randint(1,10)
print(random_integer)
if random_integer % 2 == 1:
    print("Head")
else:
    print("Tail")