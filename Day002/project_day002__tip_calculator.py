# 1. Welcome to the tip calculator!
# 2. What was the total bill? $ # 100
# 3. How much tip would you like to give? 10, 12, or 15? # 15
# 4. How many people to split the bill? # 3
# 5. Each person should pay: $38.33

print("Welcome to the tip calculator!")
user_bill = float(input("What was the total bill? $"))
user_tip = int(input("How much tip would you like to give (%age)? "))
bill_with_tip = user_bill + (user_tip/100 * user_bill)
split_number = int(input("How many people to split the bill? "))
bill_per_person = round(bill_with_tip/split_number, 2)
print(f"Each person should pay: ${bill_per_person}")