"""
Caesar Cipher.
Project for Angela Wu's 100 days of code challenges.
Day # 8
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ]


# TODO 2: loop asking the user till inputs "no"

def caesar(order: str, text: str, shift_key: int):
    """Function to encode/decode a given message."""
    new_message = ""
    # To substract the given shift_key and decode the message
    if order == "decode":
        shift_key *= -1

    for char in text:
        # To exclude symbols and numbers from bein encrypted/decrypted
        if char in alphabet:
            index = alphabet.index(char)
            cipher_index = index + shift_key
            cipher_char = alphabet[cipher_index]
            new_message += cipher_char
        # Char not in alphabet
        else:
            new_message += char

    print(f"Your {order}d message is: {new_message}")


# def encrypt(original_msg: str, shift_key: int):
#     encrypted_msg = ""
#     for letter in original_msg:
#         # To exclude symbols and numbers from being encrypted
#         if letter not in alphabet:
#             encrypted_msg += letter
#         else:
#             original_index = alphabet.index(letter)
#             encrypted_index = original_index + shift_key
#             encrypted_letter = alphabet[encrypted_index]
#             encrypted_msg += encrypted_letter
#
#     print(f"The encrypted message is: {encrypted_msg}")
#
#
# def decrypt(encrypted_msg: str, shift_key: int):
#     decrypted_msg = ""
#     for letter in encrypted_msg:
#         # To exclude symbols and numbers from being decrypted
#         if letter not in alphabet:
#             decrypted_msg += letter
#         else:
#             encrypted_index = alphabet.index(letter)
#             decrypted_index = encrypted_index - shift_key
#             decrypted_letter = alphabet[decrypted_index]
#             decrypted_msg += decrypted_letter
#
#     print(f"The decoded message is: {decrypted_msg}")
#

# Instruct whether to encrypt or decrypt a message


# Instruction

def instruct():
    """Order given by the user to encrypt or decrypt a message."""
    print('Type "encode" to encrypt your message or "decode" to decrypt a message')
    instruction = input().lower()
    # Check if the right instruction was given by the user input
    while instruction != "encode" and instruction != "decode":
        print(f'"{instruction}" unknown instruction')
        print('Type "encode" to encrypt your message or "decode" to decrypt a message')
        instruction = input().lower()
    return f"{instruction}"


def msg():
    """Message to encrypt/decrypt."""
    print("Type the message")
    message = input().lower()
    return message


def shift_code():
    """Shift to encrypt/decrypt message - shift_key."""
    while True:
        print("Type the shift number")
        shift = input()
        # Check if it's a valid shift value
        try:
            # For indexing purposes the alphabet is repeated. Only makes sense to
            # shift the msg using the first alphabet of the list
            shift = int(shift) % 26
            if shift < 1:
                print("Shift out of range")
            break

        except ValueError:
            print("Only numbers")

    return shift


caesar(order=instruct(), text=msg(), shift_key=shift_code())

# Repeat
while True:
    print("\nDo you want to encode/decode a message again?\nType 'yes' or 'no'.")
    repeat = input().lower()
    if repeat == "no":
        break
    elif repeat == "yes":
        caesar(order=instruct(), text=msg(), shift_key=shift_code())
    else:
        print(f"{repeat} unknown instruction. Type 'yes' or 'no'.")


