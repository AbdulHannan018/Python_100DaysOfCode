# print("Hello " + input("What is your name?") + "!")  # concatenation of str and input
#
# name = "Jack"
# print(name)
#
# name = "Jack Sparrow"
# print(name)  # variable reassignment: var. name has been reassigned as python is dynamic
#
# name = input("Enter you name:")
# print(name)
# print("Length of name:", len(name))
#
# # better way to calculate length
# length = len(name)
# print("Length of name:", length)


"""
    We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice.
     Write 3 lines of code to switch the contents of the variables.
     You are not allowed to type the words "milk" or "juice".
     You are only allowed to use variables to solve this exercise."""

glass1 = "milk"
glass2 = "juice"
print(f'glass1: {glass1}, glass2: {glass2}')
glass3 = glass1
glass1 = glass2
glass2 = glass3
print(f'glass1: {glass1}, glass2: {glass2}')