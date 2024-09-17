import random
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

choices = [rock, paper, scissors]

# While loop: If choice is valid, game will continue, if choice is invalid it will ask again to type an option
while True:
    player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
    if player_choice not in ["0", "1", "2"]:
        print("INVALID CHOICE, PLEASE TRY AGAIN")
        continue
    else:
        print("Your choice is" + choices[int(player_choice)])
    break

computer_choice = random.choice(choices)
print("The computer choice is: " + computer_choice)

# No winner
if (choices[int(player_choice)]) == computer_choice: print("No winner. Try Again!")

# Player is the winner
if player_choice == "1" and computer_choice == rock: print("Congratulation, You Won!")
if player_choice == "2" and computer_choice == paper: print("Congratulation, You Won!")
if player_choice == "0" and computer_choice == scissors: print("Congratulation, You Won!")

# Computer is the winner
if player_choice == "1" and computer_choice == scissors: print("The Computer Won")
if player_choice == "2" and computer_choice == rock: print("The Computer Won")
if player_choice == "0" and computer_choice == paper: print("The Computer Won")