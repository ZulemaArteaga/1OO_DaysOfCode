'''The objective is to take the inputs from the user to these questions and then generate a random password. '''

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
while True:
    # Prompts the user for integer input, validates it, and repeats if invalid.
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        break
    except ValueError:
        print("INVALID OPTION. Please select a numeric value")


# EASY VERSION. Password with Pattern: First Letters then Symbols and last Numbers
password = []
for letter in range(nr_letters):
    password.append(random.choice(letters))

for symbol in range(nr_symbols):
    password.append(random.choice(symbols))

for number in range(nr_numbers):
    password.append(random.choice(numbers))

print("Your Password is: " + ''.join(password))
print("This password follow a sequence: letter > symbols > numbers\n")


# HARD VERSION. Password does not follow a pattern
password = []
for each in range(nr_letters) and range(nr_symbols) and range(nr_numbers):
    chars = random.choice(letters) + random.choice(symbols) + random.choice(numbers)
    password.append(chars)

    random.shuffle(password)

print("Your Password is: " + ''.join(password))
print("This password doesn't follow a pattern")

