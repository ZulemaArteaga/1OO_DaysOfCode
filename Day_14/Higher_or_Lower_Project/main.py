"""Who has more followers Game.
A game where you guess who has more followers, and it keeps track of your score.
"""

from game_data import data
import random

def game():
    """Try to guess who has more followers"""
    score = 0

    a = random.choice(data)
    b = random.choice(data)

    while True:
        if a == b: # If random choices for a and b are the same it will pass without printing them
            b = random.choice(data)
            continue

        print(f'Compare A: {a['name']}, {a['description']}, from {a['country']}')
        print(f'Compare B: {b['name']}, {b['description']}, from {b['country']}')

        guess = input('Who has more followers? Type "A" or "B": ').upper()
        print("\n" * 10)

        if a['follower_count'] == b['follower_count']:
            print("It's a draw")

        elif guess == "A":
            if a['follower_count'] < b['follower_count']:
                print(f"Sorry, that's wrong. Your score is: {score}.")
                break
            if a['follower_count'] > b['follower_count']:
                score += 1
                print(f'You are right. {a['name']} has more followers. Your score is: {score}.\n')
                a = b  # assign the value of b to a for the next round

        elif guess == "B":
            if a['follower_count'] > b['follower_count']:
                print(f"Sorry, that's wrong. Your score is: {score}.")
                break
            if a['follower_count'] < b['follower_count']:
                score += 1
                print(f'You are right.{b['name']} has more followers. Your score is: {score}.\n')
                a = b # assign the value of b to a for the next round
        else:
            print('Invalid Option. Please Type "A" or "B"')

game()
