import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def guessing_process(attempts, number):
    print(f"You have {attempts} attempts to guess the number!")
    guess = int(input("Make a guess:"))
    if number > guess:
        attempts -= 1
        print("To low!")
    elif number < guess:
        attempts -= 1
        print("To high!")
    else:
        attempts = 0
        print(f"You got it! The number is {guess}!")

    return attempts

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking a number between 1 and 100.")

    number = random.randint(1,100)
    print(f"The number is {number}!!!!!!")
    level = input("Choose a difficulty. Type 'easy' or 'hard'. ")

    if level == 'easy':
        attempts = EASY_LEVEL_TURNS
        while attempts > 0:
            attempts = guessing_process(attempts, number)
            if attempts == 0:
                print("Game over!")
    elif level == 'hard':
        attempts = HARD_LEVEL_TURNS
        while attempts > 0:
            attempts = guessing_process(attempts, number)
            if attempts == 0:
                print("Game over!")
    else:
        print("Incorrect input!")


game()













