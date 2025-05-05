# Subscripting
print("Hello"[0])
print("Hello"[-1])  # or
print("Hello"[4])

# Strings
print("123" + "345")

# Integers:Whole numbers
print(123 + 345)

# Large Integers: separated by underscores, underscores ignored in output
print(123_456_789_0)

# Float: With a decimal point
print(123.00)

# Boolean
print(True)
print(False)

# Type Checking
print(type("Hello"))
print(type(123))
print(type(123.0))
print(type(True))

# Type Conversion and Type Casting
print(int("123") + int("456"))

# Concatenation using Type Conversion
user_name = input("Enter you name: ")  # -> str
length_of_user_name = len(user_name)  # -> int
print("Length of your name is " + str(length_of_user_name))  # TypeError: can only concatenate str (not "int") to str
                                                                                # coz len() gives int as output

x = int("5")
print("Type of x is :", type(x))
