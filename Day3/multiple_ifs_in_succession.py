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


