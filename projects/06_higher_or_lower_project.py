from game_data import data
import random

def comparing_followers(data_a, data_b):
    if data_a >= data_b:
        return "A"
    else:
        return "B"


def choose_data():
    choice = random.choice(data)
    data.remove(choice)

    return choice


A = choose_data()

continue_game = True
score = 0
while len(data) > 0 and continue_game:
    print(len(data))
    B = choose_data()

    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}")
    print("vs")
    print(f"Compare B: {B['name']}, a {B['description']}, from {B['country']}")

    winner_followers = comparing_followers(A['follower_count'], B['follower_count'])

    guess = input("Who has more followers? 'A' or 'B'?")

    if guess == winner_followers:
        score += 1
        if winner_followers == "B":
            A = B

        if len(data) == 0:
            print(f"Game over! Your score is {score}")
    else:
        print(f"Game Over! Your score is {score}!")
        continue_game = False

