# Ascii art
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island. Your mission is to find the treasure.")
choice1 = input("You're at the crossroad."
                "Enter your choice (left or right): ").lower()

if choice1 == "right":
    print("You're one step closer to the treasure.")
    choice2 = input("You've reached at the lake."
                    "Enter your choice (swim or wait): ").lower()
    if choice2 == "wait":
        print("You're one step closer to the treasure.")
        choice3 = input("You've reached in front of a house that seems haunted."
                        "Enter the door you want to enter from (red, blue or black): ").lower()

        if choice3 == "blue":
            print("Congratulations! You've found the treasure.")
        elif choice3 == "black":
            print("Game over! You fell into the hole.")
        elif choice3 == "red":
            print("Game over! You're burnt.")
        else:
            print("Game over! Invalid choice")

    elif choice2 == "swim":
        print("Game over! You're eaten by aabi hayaat.")
    else:
        print("Game over! Invalid choice")

elif choice1 == "left":
    print("Game over! You chose the wrong path.")
else:
    print("Game over! Invalid choice")
