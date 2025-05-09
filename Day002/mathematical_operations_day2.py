#  Priority of mathematical operations
#  PEMDAS
# 1. Parenthesis
# 2. Exponentiation
# 3. Multiplication or Division -> Left one will be preferred, either * or /
# 4. Addition or Subtraction -> Left one will be preferred, either + or -
# PEMDAS LR

print(6 + 3)
print(6 - 3)
print(6 * 3)
print(3 ** 3)  # Exponentiation
print(6 / 4)  # Division: contains decimal part
print(type(6 / 4))  # implicit type casting: integers -> float
print(6 // 4)  # Floor Division: doesn't contain decimal part
print(type(6 // 4))
print(6 % 4)  # Modulus: Gives the remainder

print(3 * 3 + 3 / 3 - 3)  # important datatype
# Change the code so it outputs 3
print(3 * (3 + 3) / 3 - 3)
print(3 + 3 * 3 / 3 - 3)
