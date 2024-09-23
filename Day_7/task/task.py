import random
from hangman_words import word_list
from hangman_art import stages

chosen_word = random.choice(word_list)
print(chosen_word)

# Printing"_" for each letter of the random word_list
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
lives = 6
correct_letters = []

while not game_over:
    print(f"You have: {lives} lives left \n")
    guess = input("Guess a letter: ").lower()[0] # Index ensures that only one letter is considered

    display = ""

    for letter in chosen_word:
        # First, check if the letter matches the chosen_word.
        # Then, reveal the word letter by letter with each loop until the entire word is shown
        # If letter doesn't match the chosen_word, it displays "_"
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # This verifies the guess input is a letter
    if not guess.isalpha(): print("INVALID OPTION. Please type 1 letter from the alphabet")
    # If the letter isn't in the chosen_word, it prints the letter and deducts one life.
    elif guess not in chosen_word:
        print(f'"{str(guess)}" is not in the word')
        lives -= 1

        # If lives is 0, game is over
        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE. The word was: {str(chosen_word)}**********************")

    # If no "_" prints "YOU WIN"
    if "_" not in display:
        game_over = True
        print("****************************CONGRATULATIONS. YOU WON!****************************")

    print(stages[lives])



