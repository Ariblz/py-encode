# Worst code
import random


def encrypt_text(text, seed):
    random.seed(seed)
    encrypted_text = ''
    for char in text:
        encrypted_char = chr(ord(char) + random.randint(1, 100))
        encrypted_text += encrypted_char
    return encrypted_text


def decrypt_text(encrypted_text, seed):
    random.seed(seed)
    decrypted_text = ''
    for char in encrypted_text:
        decrypted_char = chr(ord(char) - random.randint(1, 100))
        decrypted_text += decrypted_char
    return decrypted_text


print("What is your seed? (only numbers)")

seed = int(input())

print("And what is your text?")

message = str(input())

print("You want to encrypt message or decrypt it? (1 or 2)")

choice = int(input())

if choice == 2:
    a = decrypt_text(message, seed)
    print("Decrypted message:", a)
if choice == 1:
    a = encrypt_text(message, seed)
    print('Encrypted message:', a)
