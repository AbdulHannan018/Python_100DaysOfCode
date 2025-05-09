# print("Welcome to Python Pizza Delivery!")
# size = input("Enter the pizza size you want (s, m or l): ")
# pepperoni = input("Do you want pepperoni (y or n)? ")
# extra_cheese = input("Do you want extra cheese (y or n)? ")
# bill = 0
#
# if size == "s":
#     bill += 15
#     if pepperoni == "y":
#         bill += 2
# elif size == "m":
#     bill += 20
#     if pepperoni == "y":
#         bill += 3
# elif size == 'l':
#     bill += 25
#     if pepperoni == "y":
#         bill += 3
# else:
#     print("Invalid choice.")
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your total bill is ${bill}.")


# Better solution ig
print("Welcome to Python Pizza Delivery!")
size = input("Enter the pizza size you want (s, m or l): ")
pepperoni = input("Do you want pepperoni (y or n)? ")
extra_cheese = input("Do you want extra cheese (y or n)? ")
bill = 0

# size
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == 'l':
    bill += 25
else:
    print("Invalid choice.")

# pepperoni
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3

# Cheese
if extra_cheese == "y":
    bill += 1

print(f"Your total bill is ${bill}.")


