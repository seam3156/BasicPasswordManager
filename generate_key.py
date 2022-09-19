#! /bin/python3


from cryptography.fernet import Fernet


def decrypt(key):
    with open("passwords.txt", "rb") as file:
        contents = file.read()
    with open("passwords.txt", "wb") as file:
        decrypted_contents = Fernet(key).decrypt(contents)
        file.write(decrypted_contents)

def encrypt(key):
    with open("passwords.txt", "rb") as file:
        contents = file.read()
    with open("passwords.txt", "wb") as file:
        encrypted_contents = Fernet(key).encrypt(contents)
        file.write(encrypted_contents)

with open("passkey.key", "rb") as thekey:
    key = thekey.read()
decrypt(key)

key = Fernet.generate_key()
with open("passkey.key", "wb") as thekey:
    thekey.write(key)

encrypt(key)
