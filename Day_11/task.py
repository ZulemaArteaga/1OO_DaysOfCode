"""Blackjack Game House Rules
The deck is unlimited in size.
There are no jokers.
The Jack/Queen/King all count as 10.
The Ace can count as 11 or 1.
Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

The cards in the list have equal probability of being drawn.
Cards are not removed from the deck as they are drawn.
The computer is the dealer."""

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_score = 0
computer_score = 0

def get_random_cards(num_cards=0):
    """
    Function to help get random cards.
    Add the number of cards needed when calling this function
    :param num_cards: The amount of cards to draw
    :return: A list of numbers (the cards) if more than 2. A single Int if 1
    """
    cards_drawn = random.choices(cards, k=num_cards)
    return cards_drawn if num_cards > 1 else cards_drawn[0]

def need_to_change_ace_value(cards, score):
    """
    If an ace (represented as 11) is drawn and the total score goes over 21,
    count the ace as 1 instead.

    Parameters:
    - cards: list of cards for the user or computer.
    - score: current total score of user or computer.

    Returns:
    Updated scores for both user or computer after adjusting for ace values if needed.
    """
    while score > 21 and 11 in cards:
        for card in range(len(cards)):
            if cards[card] == 11:
                # print("Since the score went over 21 and there is an ace in the cards, the ace's value is now 1")
                cards[card] = 1
    score= sum(cards)
    return score

def want_to_play_blackjack_game():
    """
    Asks the user to decide if he wants to play Blackjack
    """
    while True:
        play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': \n").lower()
        if play == 'n':
            print("Good Bye")
            break
        elif play == 'y':
            print("\n" * 20)
            play_blackjack()
        else:
            print("Invalid option. Please type 'y' or 'n'.")

def play_blackjack():
    """
    Function to execute the Blackjack game.
    """
    end_game = False

    # The user and computer should each get 2 random cards.
    user_cards = get_random_cards(2)
    computer_cards = get_random_cards(2)

    # Add up the user's and the computer's scores
    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f'Your cards are: {user_cards},\n'
          f'Your total score is: {user_score}')

    # Does the user or computer have a blackjack? (ace + 10)
    if user_score == 21 or computer_score == 21:
        if user_score == 21 and computer_score == 21:
            print("\nBoth got Blackjack! It's a Draw."
            f"\n Computer cards: {computer_cards}"
            f"\n Your cards: {user_cards}")
        elif user_score == 21:
            print("\nBlackjack! You won\n"
                  f"Your cards are: {user_cards}")
        else:
            print(f"\nBlackjack! The computer won.\n"
                  f"The computer cards are: {computer_cards}")
        return

    # If none have Blackjack: Is user's score over 21?
    need_to_change_ace_value(user_cards, user_score)

    while not end_game:
        # If User Score is not over 21: Ask the user if he wants to get another card.
        if user_score > 21 :
            print("You loose. Your score is over 21")
            break

        # Ask the user if he wants to get another card
        another_card = input("Do you want to get another card? Type 'y' or 'n': \n").lower()
        if another_card not in ('y', 'n'): print("Invalid option. Type 'y' or 'n': ")

        elif another_card == 'y':
            # User draw another card
            user_cards.append(get_random_cards(1)) # User gets another ramdom card and append it to his user_card list
            user_score = sum(user_cards)
            need_to_change_ace_value(user_cards, user_score) # If user have an ace and value is over 21, the ace value will change to 1
            user_score = sum(user_cards) # Need to sum the cards again, in case the ace value 11 changed to 1
            print(f'Your cards are: {user_cards}\n'
                  f'Your total score is: {user_score}')

            if user_score == 21:
                print("\nBlackjack. You win!")
                break
            elif user_score > 21:
                print(f"\nYou lose. Your score is {user_score}, which is over 21.")
                break

        elif another_card == 'n':
            while computer_score < 17:  # Computer plays, if score is less than 17, keep drawing cards.
                computer_cards.append(get_random_cards(1))  # Computer gets another ramdom card and append it to his computer_card list
                computer_score = sum(computer_cards)

                need_to_change_ace_value(computer_cards, computer_score)  # If computer have an ace and value is over 21, the ace value will change to  1
                computer_score = sum(computer_cards)  # Need to sum the cards again, in case the ace value 11 changed to 1

            # Computer gone over 21?
            if computer_score > 21:
                print("\nComputer went over 21. You win!\n"
                      f"The computer score is {computer_score}. Cards: {computer_cards}\n")
                end_game = True

            else:
                # Compare user score with computer score to see if user score is higher
                print("\nThe winner is:")
                if user_score > computer_score:
                    print(f"You win! \n"
                          f"Your score is: {user_score}. Cards: {user_cards}\n"
                          f"The computer score is: {computer_score}. Cards: {computer_cards}")
                elif user_score < computer_score:
                    print(f"The computer wins!\n"
                          f"Your score is {user_score}. Cards: {user_cards}\n"
                          f"The computer score is {computer_score}. Cards: {computer_cards}")
                else:
                    print(f"It's a draw!\n"
                          f"Your score: {user_score}, Cards: {user_cards}\n"
                          f"Computer's score: {computer_score}, Cards: {computer_cards}")
                end_game = True

want_to_play_blackjack_game()
