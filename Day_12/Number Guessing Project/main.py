'''Number Guessing Proyect
The player guesses a number chosen by the computer.
The game provides hints if the guess is too high or too low
and ends when the player guesses correctly or runs out of attempts.'''

import random

computer_number = random.randint(1, 101)
# print(computer_number)

print("\nWelcome to the Guessing Game. \nGuess the number I have, the number is between 1 and 100. \n")
game_over = False

while not game_over:

    begin_game = str(input("Choose the difficulty: type 'h' for hard or 'e' for easy: ").lower())

    if begin_game in ('e', 'h'):
        initial_attempts = 5
        attempts = initial_attempts
        if begin_game == 'e':
            initial_attempts = 10
            attempts = initial_attempts
    else:
        # If input is not 'h' or 'e', it will enter the loop again
        continue

    while True:
        try:
            guessed_number = int(input("Make a guess: "))

            if (guessed_number > 100) or (guessed_number < 1):
                print("Make a guess, please type a number between 1 and 100: ")

            elif guessed_number == computer_number:
                print(f"\nYou got it! The number is: {computer_number}")
                break

            elif guessed_number != computer_number:
                attempts -= 1
                if attempts > 0:
                    print(f"Incorrect. Try again. You have {attempts} left.")
                    if guessed_number < computer_number:
                        print("Too low.")
                    else:
                        print("Too high.")
                else:
                    print(f"\nSorry! You've used all your attempts.\n"
                          f"The number was: {computer_number}")
                    break
        except:
            # If player types a letter instead of a number, system will ask to type a number
            print("Invalid option. Please type a number between 1 and 100.")

    game_over = True
