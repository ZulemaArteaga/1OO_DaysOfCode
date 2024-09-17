import random
import emoji

rock = emoji.emojize(":raised_fist:")
paper = emoji.emojize(":hand_with_fingers_splayed:")
scissors = emoji.emojize(":victory_hand:")

choices = [rock, paper, scissors]

# While loop: If choice is valid, game will continue, if choice is invalid it will ask again to type an option
while True:
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    if player_choice not in ["0", "1", "2"]:
        print("INVALID CHOICE, PLEASE TRY AGAIN")
        continue
    else:
        print("Your choice is " + choices[int(player_choice)])
    break

computer_choice = random.choice(choices)
print("The computer choice is: " + computer_choice)

# No winner
if (choices[int(player_choice)]) == computer_choice: print("No winner. Try Again!")
# Player is the winner
elif (player_choice == "1" and computer_choice == rock or
        player_choice == "2" and computer_choice == paper or
        player_choice == "0" and computer_choice == scissors):
    print("Congratulation, You Won!")
# ELSE statement covers when the Computer wins
else: print("The Computer Won")
