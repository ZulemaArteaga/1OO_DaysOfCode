import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''Building an encryption and decryption program using the Caesar cipher. 
https://en.wikipedia.org/wiki/Caesar_cipher
'''
print(art.logo)
def game():
    game_over = False

    # Input: encode or decode
    while not game_over:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]: break # If typed correct words, will break this loop
        else: print("INVALID OPTION. Try again")

    # Input: type message
    text = input("Type your message:\n").lower()

    # Input: type the shift
    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break  # If int is given, will break this loop
        except ValueError:
            print("INVALID OPTION. Please enter a number.")

    # Script for encode
    def encrypt(original_text, shift_amount):
        new_text_encrypt = []
        for letter in original_text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_index = (letter_index + shift_amount) % len(alphabet) # See notes below
                new_letter = alphabet[new_index]
                new_text_encrypt.append(new_letter)
            else:
                new_text_encrypt.append(letter)  # Unmodified for non-alphabet characters
        print("\nThe encode text is: " + "".join(new_text_encrypt))

    # Script for decode
    def decrypt(original_text, shift_amount):
        new_text_decrypt = []
        for letter in original_text:
            if letter in alphabet:
                letter_index = alphabet.index(letter)
                new_index = (letter_index - shift_amount) % len(alphabet) # See notes below
                new_letter = alphabet[new_index]
                new_text_decrypt.append(new_letter)
            else:
                new_text_decrypt.append(letter)  # Unmodified for non-alphabet characters
        print("\nThe decode text is: " + "".join(new_text_decrypt))

    def caesar(original_text, shift_amount, encode_or_decode):
        if encode_or_decode == "encode":
            encrypt(original_text, shift_amount)
        elif encode_or_decode == "decode":
            decrypt(original_text, shift_amount)

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Input: Asking if you want to play again
    while True:
        play_again = input("\nWould you like to play again? Type: Yes or No \n").lower()
        if play_again == "no":
            print("Thank You for playing")
            break
        if play_again == "yes":
            print("Starting new game")
            game()
        else:
            print("INVALID OPTION. Type: yes or not")
game()


# NOTES:
# % len(alphabet): This operation is commonly used to "wrap around" an index
# If the value on the left of % is larger than or equal to len(alphabet),
# this will ensure that the value stays within the bounds of the sequence by returning a value between 0 and len(alphabet) - 1.
# For example, if alphabet is the string (with length 26),
# then 30 % len(alphabet) would be 30 % 26, which equals 4.
# This allows you to use index 4 in alphabet, which corresponds to the letter E.