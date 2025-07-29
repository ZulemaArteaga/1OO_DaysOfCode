import random
from hangman_words import word_list
from hangman_art import stages

'''Today's challenge is to create a Hangman Game,
where players must guess letters to reveal a hidden word before running out of chances.'''

chosen_word = random.choice(word_list).upper()
print(chosen_word)

# Printing"_" for each letter of the random word_list
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_ "
print("Word to guess: " + placeholder)

game_over = False
lives = 6
saved_display_letters = []
while not game_over:
    print(f"You have: {lives} lives left \n")
    guess = input("Guess a letter: ").upper()
    if len(guess) > 1: # Limits one letter in input
        print("INVALID OPTION. Please type only one character")
    elif not guess.isalpha(): # Checks if input is alphabetical
        print("INVALID OPTION. Please type 1 letter from the alphabet")
    else:
        if guess not in chosen_word:
            print(f'"{str(guess)}" is not in the word')
            lives -= 1 # If guess letter is not in the chosen word, it rests one live
        if lives <= 0: # If lives is 0, game is over
            game_over = True
            print(f"***********************YOU LOSE. The word was: {str(chosen_word)} **********************")

        display = ""
        for letter in chosen_word:
            if letter == guess: # Checks if guess letter is in the chosen_word
                display += letter + " " # Adds letter to display
                saved_display_letters.append(letter) # Save the correct guessed letter
            elif letter in saved_display_letters:
                display += letter + " " # If already guessed letter, add to display
            else:
                display += "_ " # If the guess letter is not in chosen_word, adds " _ "
        print("Word to guess: " + display)

        if "_" not in display: # If no "_" prints "YOU WIN"
            game_over = True
            print("****************************CONGRATULATIONS. YOU WON!****************************")

    print(stages[lives])