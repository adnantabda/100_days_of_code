"""
Caesar Cipher.
Project for Angela Wu's 100 days of code challenge.
Day # 8
"""

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ]


def encrypt(original_msg: str, shift_key: int):
    encrypted_msg = ""
    for letter in original_msg:
        if letter not in alphabet:
            encrypted_msg += letter
        else:
            original_index = alphabet.index(letter)
            encrypted_index = original_index + shift_key
            encrypted_letter = alphabet[encrypted_index]
            encrypted_msg += encrypted_letter

    print(f"The encrypted message is: {encrypted_msg}")


def decrypt(encrypted_msg: str, shift_key: int):
    decrypted_msg = ""
    for letter in encrypted_msg:
        if letter not in alphabet:
            decrypted_msg += letter
        else:
            encrypted_index = alphabet.index(letter)
            decrypted_index = encrypted_index - shift_key
            decrypted_letter = alphabet[decrypted_index]
            decrypted_msg += decrypted_letter

    print(f"The decoded message is: {decrypted_msg}")


# Instruct whether to encrypt or decrypt a message
print('Type "encode" to encrypt your message or "decode" to decrypt a message')
instruction = input().lower()
# Check if the right instruction was given by the user input

while instruction != "encode" and instruction != "decode":
    print(f'"{instruction}" unknown instruction')
    print('Type "encode" to encrypt your message or "decode" to decrypt a message')
    instruction = input().lower()


# Message to encrypt/decrypt
print("Type the message")
message = input().lower()


# Shift to encrypt/decrypt message
while True:
    print("Type the shift number")
    shift = input()
    # Check if it's a valid shift value
    try:
        shift = int(shift)
        # For indexing purposes the alphabet is repeated. Only makes sense to
        # shift the msg using the first alphabet of the list
        if shift < (len(alphabet) / 2):
            break
        else:
            print("Shift out of range")
    except ValueError:
        print("Only numbers")


if instruction == 'encode':
    encrypt(message, shift)
else:
    decrypt(message, shift)
