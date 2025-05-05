a = 18
print(a > 10)
print(a < 10)

# and: binary operator, A and B
print("\nand")
print(True and True)
print(True and False)

print(a > 10 and a < 10)
print(a > 10 and a < 20)  # print(10 < a < 20)  # both are the same

# or: binary operator, A or B
print("\nor")
print(True or False)
print(False or False)

print(a > 10 or a < 10)
print(a > 18 or a < 17)

# not: uniary operator, not A
print("\nnot")
print(not False)
print(not True)

print(not a > 10)
print(not a > 20)

# mixed ones
print("\nmixed ones")  # ig they are evaluated from left to right when multiple logical operators in one line
print(True and False or False)
print(True and True or False)
print(True and not True or False)

# Increased functionality with midlife crisis
print("\nmidlife crisis")
height = int(input("Enter your height (cm): "))
bill = 0
# bill = None   Q: can it be None?
if height >= 120:
    print("You can ride.")
    age = int(input("Enter your age: "))
    if age < 12:
        bill = 5
        print("Child ticket is $5")
    elif age <= 18:
        bill = 7
        print("Youth ticket is $7")
    elif age >= 45 and age <= 55:  # simpler way: 45 <= age <= 55
        print("Due to midlife crisis, your ride is free.")
    else:
        bill = 12
        print("Adult ticket is $12")

    photo = input("Do you want a photo (y/n)? ")
    if photo == "y":
        bill += 3

    print(f"Your total bill is ${bill}.")  # will always execute after if condition is executed whether True or False
    # if True then bill += 3, if False then bill = bill
else:
    print("You are not tall enough to ride.")