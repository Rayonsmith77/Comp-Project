import pyperclip,time,sys,json
from pathlib import Path

fname = "pass.txt"
filedir = Path("pass.txt")
if filedir.is_file():
    open(fname,"r+")
    passwords = json.load(open(fname))
else:
    open(fname,"w")
    passwords = {}
    print("This ")

def menu():
    print("---------------------")
    print("HOTEL LOCKER")
    print("---------------------")
    print("1. Find password")
    print("2. Add password")
    print("3. Exit")
    print("---------------------")

    option = int(input("Enter option:"))

    while option:
        if option == 1: 
            fPass()
        elif option == 2:
            savePass()
        elif option == 3:
            break
        else:
            print("Invalid Option")
        print("-------------")
        option = int(input("Enter option:"))

    print("Exiting...")
    print("---------------------")


def savePass():
    account = input("Enter website\email:")
    password = input("Enter password:")
    passwords[account] = encode(password)
    json.dump(passwords, open(fname,"w"))
    print("Password Saved")

def fPass():
    account = input("Enter website\email:")
    if account in passwords.keys():
        encrypted_pass = passwords[account]
        pyperclip.copy(decode(encrypted_pass))
        print("Password copied for 10 seconds...")
        time.sleep(10)
        pyperclip.copy("")
        print("Password destroyed from clipboard")
    else:
        print("Account not found")

def encode(passwd):
    encoded_chars= []
    for i in range(len(passwd)):
        encoded_c = chr(ord(passwd[i]) - len(passwd))
        encoded_chars.append(encoded_c)
    encrypted_pass = "".join(encoded_chars)
    return encrypted_pass
        
def decode(encrypted_passwd):
    decoded_chars = []
    for i in range(len(encrypted_passwd)):
        decoded_c = chr(ord(encrypted_passwd[i]) + len(encrypted_passwd))
        decoded_chars.append(decoded_c)
    decoded_pass = "".join(decoded_chars)
    return decoded_pass

menu()


