"""
In a message the letters should be shifted in an alphabet using shift key. Number of letters to shift.
Also create a decypter for the same
"""

# TODO - create global variables: alphabet, shift key
from string import ascii_lowercase, ascii_uppercase
shift_key = 0
new_phrase = ""

# TODO - Greet the user & choose encrypt or decrypt & add phrase & key
def main():
    mode = input("Welcome to the caesar cypter!\nType 'encode' to encrypt, and 'decode' to decrypt:\n")
    while (mode.lower() != "encode") and (mode.lower() != "decode"):
        mode = input("Incorrect prompt, select again: ")

    phrase = input("Please add phrase: \n")
    global shift_key, new_phrase
    shift_key = input("Please add a shift key number: \n")
    while not shift_key.isnumeric():
        shift_key = input("Shift key, must be a number. Try again: ")
    shift_key = int(shift_key)
    
    cyper(phrase, mode)

    print(f"Your new phrase is: {new_phrase}")


# TODO - Encrypt - make simpler, check for edge case - z
def cyper(phrase, mode):
    global new_phrase


    for letter in phrase:
       if letter.islower():
           position = ascii_lowercase.index(letter)

           #Accounting for overflow
           overflow_position = position + shift_key
           if overflow_position > 25:
               overflow_position -= 26
    
            
           if mode == "encode":
               new_phrase += ascii_lowercase[overflow_position]
           else:
               new_phrase += ascii_lowercase[position - shift_key]
       elif letter.isupper():
           position = ascii_uppercase.index(letter)

            #Accounting for overflow
           overflow_position = position + shift_key
           if overflow_position > 25:
               overflow_position -= 26

            
           if mode == "encode":
               new_phrase += ascii_uppercase[overflow_position]
           else:
               new_phrase += ascii_uppercase[position - shift_key]
    return new_phrase

if __name__ == "__main__":
    main()