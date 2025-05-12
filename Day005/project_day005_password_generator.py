import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

# # Angela's Method

# # Easy Level
# password_str = ''
# for char in range(number_letters):
#     password_str += random.choice(letters)
#
# for symbol in range(number_symbols):
#     password_str += random.choice(symbols)
#
# for number in range(number_numbers):
#     password_str += random.choice(numbers)
#
# print(password_str)

password_list = []

for char in range(number_letters):
    password_list.append(random.choice(letters))

for symbol in range(number_symbols):
    password_list.append(random.choice(symbols))

for number in range(number_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

# print(''.join(password_list))

password = ''
for each_item in password_list:
    password += each_item

print(f'The password is: {password}')



# # # Angela's Method Explanation
# password = ''
# for char in range(number_letters):  # or for char in range(1, number_letters+1):  # or for char in range(0, number_letters):
#     password += random.choice(letters)     # random_letter = random.choice(letters)     # password += random_letter
#     # print(password)  # to see change after each iteration
# # print(f"Password letters: {password}")
#
# for symbol in range(number_symbols):
#     password += random.choice(symbols)
#     # print(password)  # to see change after each iteration
# # print(f"Password letters and symbols: {password}")
#
# for number in range(number_numbers):
#     password += random.choice(numbers)
#     # print(password)  # to see change after each iteration
# # print(f"Password letters, symbols and numbers: {password}")



# # My Method
# password = ''
# random_letters = random.sample(letters, number_letters)
# random_numbers = random.sample(numbers, number_numbers)
# random_symbols = random.sample(symbols, number_symbols)
#
# random_list = []
# random_list.extend(random_numbers)
# random_list.extend(random_symbols)
# random_list.extend(random_letters)
#
# print(random_list)
#
# # list to string conversion
# password = password.join(random_list)
# print(password)
#
# # Shuffling the password -> str
# password = ''.join(random.sample(password, len(password)))
# print(password)