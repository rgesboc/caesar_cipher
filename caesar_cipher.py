alphabet = {chr(i+64):i for i in range(1,27)}

def setup_cipher():
    while True:
        try:
            cipher_key = int(input("What is the cipher key you are using for the Caesar Cipher? Please provide a number between 1-26.\n"))
            if cipher_key < 27 and cipher_key > 0:
                break
            else:
                print("Sorry, please enter an integer between 1-26")
                continue
        except:
            print("Sorry, you did not enter an integer.")
            continue

    return cipher_key
    
def validate_string(encode_decode):
    valid_string = False
    while valid_string == False:  
        text = input(f"Please enter a valid string to {encode_decode}:\n").upper()
        for chars in text:
            if chars in alphabet.keys():
                continue
            else:
                print("Sorry that is not a valid string!")
                valid_string = False
                break
        else:
            valid_string = True
    
    return text

def encode(cipher_key,text):
    encoded = ""
    for chars in text:
        char_value = alphabet[chars] + cipher_key
        if char_value > 26:
            char_value -= 26
            encoded += list(alphabet.keys())[list(alphabet.values()).index(char_value)]
        else:
            encoded += list(alphabet.keys())[list(alphabet.values()).index(char_value)]
    return encoded

def decode(cipher_key,encoded):
    decoded = ""
    for chars in encoded:
        char_value = alphabet[chars] - cipher_key
        if char_value < 1:
            char_value += 26
            decoded += list(alphabet.keys())[list(alphabet.values()).index(char_value)]
        else:
            decoded += list(alphabet.keys())[list(alphabet.values()).index(char_value)]
    return decoded

if __name__ == "__main__":
    keep_going = True
    while keep_going == True:
        choice = input("Would you like to encode or decode a string?\n").capitalize()
        if choice == "Encode":
            print("You've chosen to encode a string of text.")
            cipher_key = setup_cipher()
            text = validate_string("encode")
            encoded = encode(cipher_key,text)
            print("You have encoded " + text + " and got " + encoded)
        elif choice == "Decode":
            print("You've chosen to decode a string of text.")
            cipher_key = setup_cipher()
            text = validate_string("decode")
            decoded = decode(cipher_key,text)
            print("You have decoded " + text + " and got " + decoded)
        else:
            print("Please enter a valid response.")

        while True:
            game_on = input("Would you like to continue encoding or decoding strings?(yes or no)\n").capitalize()

            if game_on == "Yes":
                keep_going = True
                break
            elif game_on == "No":
                keep_going = False
                break
            else:
                print("Please enter a valid response.")