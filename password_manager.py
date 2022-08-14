#! /bin/python3

from cryptography.fernet import Fernet
options = ["l", "a", "q"]

#reads encryption key
with open("passkey.key", "rb") as thekey:
    key = thekey.read()

#lists all current passwords
def listpasswords():
    with open("passwords.txt", "r") as file:
        contents = file.read()
        print(contents)

#adds a new password
def addpassword(password):
    with open("passwords.txt", "a") as file:
        file.write(password+"\n")

#encrypts the passwords
def encrypt(key):
    with open("passwords.txt", "rb") as file:
        contents = file.read()
    with open("passwords.txt", "wb") as file:
        encrypted_contents = Fernet(key).encrypt(contents)
        file.write(encrypted_contents)

#decrypts the password
def decrypt(key):
    with open("passwords.txt", "rb") as file:
        contents = file.read()
    with open("passwords.txt", "wb") as file:
        decrypted_contents = Fernet(key).decrypt(contents)
        file.write(decrypted_contents)

#main program
decrypt(key)

print("\nPASSWORD MANAGER")
while True:
    option=input("[List passwords(l)] | [Add password(a)] | [Quit(q)]\n").lower()
    if option not in options:
        continue

    if option == "l":
        print("\nPasswords:")
        listpasswords()

    elif option == "a":
        newpass = input("\nenter new password: ")
        addpassword(newpass)
        print("password added\n")
    else:
        break

encrypt(key)
