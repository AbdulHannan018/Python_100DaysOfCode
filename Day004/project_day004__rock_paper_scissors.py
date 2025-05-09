import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

print("Rock Paper Scissors Game")
user_choice = int(input("Enter your your choice (0 for rock, 1 for paper, 2 scissors): "))

print(f"You chose: {user_choice}")
print(rps[user_choice])

computer_choice = random.randint(0, 2)

print(f"Computer chose: {computer_choice}")
print(rps[computer_choice])

if user_choice > 2 or user_choice < 0:
    print("Invalid choice. Game Over.")
elif user_choice == computer_choice:
    print("It's a draw.")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")
elif user_choice > computer_choice:
    print("You win!")
else:
    print("You lose")
