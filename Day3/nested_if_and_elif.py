# height = int(input("Enter your height (cm): "))
# if height >= 120:
#     print("You can ride.")
#     age = int(input("Enter your age: "))
#     if age <= 18:
#         print("Pay $7")
#     else:
#         print("Pay $12")
# else:
#     print("You are not tall enough to ride.")


# IMPORTANT
# if: executes if a condition is True
# elif: executes if if condition is False and elif condition is True
# else: executes when all conditions are False

# Increased nested conditions
height = int(input("Enter your height (cm): "))
if height >= 120:
    print("You can ride.")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Pay $5")
    elif age <= 18:     # elif (age <= 18) and (age >= 12):
        print("Pay $7")
    else:
        print("Pay $12")
else:
    print("You are not tall enough to ride.")


# Increased nested conditions
height = int(input("Enter your height (cm): "))
if height >= 120:
    print("You can ride.")
    age = int(input("Enter your age: "))
    if age < 12:
        print("Pay $5")
    elif age <= 18:
        print("Pay $7")

    elif age <= 22:
        print("Pay $8")

    else:
        print("Pay $12")
else:
    print("You are not tall enough to ride.")