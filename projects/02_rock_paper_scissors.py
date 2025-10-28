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

import random

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors."))

print("Your choice:")
if user_choice >= 0 and user_choice <= 2:
    print(game_images[user_choice])

number = random.randint(0,2)
print("Computers choice:")
print(game_images[number])

if user_choice > 3 or user_choice <0:
    print("Invalid inputs!")
elif user_choice == number:
    print("It's a draw!")
elif user_choice == 0 and number ==1:
    print("You lose!")
elif user_choice == 0 and number == 2:
    print("You win!")
elif user_choice == 1 and number == 0:
    print("You win! ")
elif user_choice == 1 and number == 2:
    print("You lose!")
elif user_choice == 2 and number == 0:
    print("You lose!")
elif user_choice == 2 and number == 1:
    print("You win!")




