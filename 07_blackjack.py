from art import logo
import random

game = True
while game:

    play = input("Do you want to play the game of blackjack? Type 'y' or 'n'.").lower()

    if play == 'y':
        print(logo)
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        players_cards = []
        computer_cards = []

        players_cards.extend([random.choice(cards), random.choice(cards)])
        players_score = sum(players_cards)

        computer_cards.extend([random.choice(cards), random.choice(cards)])
        computer_score = sum(computer_cards)

        print(f"Your cards are {players_cards} . Your score is {players_score}.")
        print(f"The computer's first card is {computer_cards[0]}")
        print(f"The computer score is {computer_score}")

        drawing_cards = True
        # proces izvlacenja karataa, trebam mi while petlja koja ce se vrtiti dok svi ne odustanu od izvlacenja karata
        while drawing_cards:
            another_card = input("Type 'y' if you want another car, or 'n' if you want to pass!").lower()

            if another_card == "y":
                new_card = random.choice(cards)
                print(f"Your new card is {new_card}")
                players_cards.append(new_card)
                players_score = sum(players_cards)
                if players_score > 21 and 11 in players_cards:
                    players_cards.remove(11)
                    players_cards.append(1)
                players_score = sum(players_cards)
            else:
                drawing_cards = False

        while computer_score <= 17:
            new_card = random.choice(cards)
            computer_cards.append(new_card)
            computer_score = sum(computer_cards)
            if computer_score > 21 and 11 in computer_cards:
                computer_cards.remove(11)
                computer_cards.append(1)
            computer_score = sum(computer_cards)


        print(f"Final players score and cards are: {players_score}, {players_cards}")
        print(f"Final computer score and cards are: {computer_score}, {computer_cards}")

        if players_score == computer_score:
            print("It's a draw!")
        elif computer_score > 21 and players_score < 21:
            print("Player is the winner!")
        elif computer_score < 21 and players_score > 21:
            print("Computer is the winner!")
        elif computer_score > 21 and players_score > 21:
            print("There are no winners!")
        elif computer_score < 21 and players_score < 21 and computer_score > players_score:
            print("The computer is the winner!")
        elif computer_score < 21 and players_score < 21 and players_score > computer_score:
            print("The player is the winner!")

        print("This hand is over!")

    else:
        print("Bye bye!")
        game = False

