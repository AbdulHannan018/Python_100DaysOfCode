# Modulo Operator: Binary operator-> goes b/w two numbers
#                   Gives remainder after division
print(10 % 5)
print(10 % 3)

# Check Odd or Even
user_input = int(input("Enter the number: "))
remainder = user_input % 2
if remainder == 0:
    print("The given number is Even")
else:
    print("The given number is Odd.")
# Another solution (better)
user_input = int(input("Enter the number: "))
if user_input % 2 == 0:
    print("Even number")
else:
    print("Odd number")

