import random
friends = ["Zuzi", "Impatient", "Ibrahim", "Abdul"]
person_paying_bill = random.choice(friends)
print(person_paying_bill)

# another solution
random_index = random.randint(0,3)
print(friends[random_index])

