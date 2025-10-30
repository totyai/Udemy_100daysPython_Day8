"""
In a message the letters should be shifted in an alphabet using shift key. Number of letters to shift.
Also create a decypter for the same
"""

# TODO - create global variables: alphabet, shift key
from string import ascii_lowercase, ascii_uppercase
shift_key = 0

# TODO - Greet the user & choose encrypt or decrypt & add phrase & key
def main():
    mode = input("Welcome to the caesar cypter!\nType 'encode' to encrypt, and 'decode' to decrypt:\n")
    while (mode.lower() != "encode") and (mode.lower() != "decode"):
        mode = input("Incorrect prompt, select again: ")

    phrase = input("Please add phrase: \n")
    shift_key = input("Please add a shift key number: \n")
    while not shift_key.isnumeric():
        shift_key = input("Shift key, must be a number. Try again: ")

    if mode == "encode":
        new_phrase = encrypt(phrase, shift_key)
    else:
        new_phrase = decrypt(phrase, shift_key)

    print(f"Your new phrase is: {new_phrase}")
# TODO - Encrypt
def encrypt(phrase, shift_key):
    for letter in phrase:
       pass 

# TODO - Decrypt message
def decrypt(phrase, shift_key):
    pass

if __name__ == "__main__":
    main()