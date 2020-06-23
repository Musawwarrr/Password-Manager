import cryptography
import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def get_key():
    print("Password: ")
    password_provided = input() # This is input in the form of a string
    password = password_provided.encode() # Convert to type bytes
    salt = b"\x92\x8d\xa7=Z\x17\x9e\x87'z9\xa3\x9f\x8bF\x15("
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
        )
    key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once

    return key

# def init_enc(key):
#     with open('info.encrypted') as f:
        


def enc_file(key, data):
        
    usr_file = 'info.encrypted'

    fernet = Fernet(key)
    enc = fernet.encrypt(data)

    with open(usr_file, 'wb') as f:
        f.write(enc)

def dec_file(key):
    user_file = 'info.encrypted'

    with open(user_file, 'rb') as f:
        data = f.read()
    
    fernet = Fernet(key)
    dec = fernet.decrypt(data)

    return dec

def terminal_disp(data):
    print("\nSite\t\t\t", "Username\t\t\t", "Password\n")
    site = data.decode("utf-8").split('\n')
    for line in site:
        word = line.split(',')
        print(word[0]+'\t\t', word[1]+'\t\t\t', word[2]+'\n')

def add_pass(key):
    data = dec_file(key)
    same = False
    while (same != True):
        username = input("Username: ")
        confirm = input("Confirm username: ")
        if username == confirm:
            same = True
    same = False        
    while (same != True):
        password = input("Password: ")
        confirm = input("Confirm password: ")
        if password == confirm:
            same = True
    site = input("Please enter the name of the site: ")
    enc = data.decode("utf-8")
    new_l = enc + site +','+ username +',' + password + '\n'
    enc_file(key, new_l.encode())
    
if __name__ == "__main__":

    key = get_key()
    data = dec_file(key) #data is formatted like "site,username,password/n"
    terminal_disp(data)
    add_pass(key)
    


    



#def search_pass():

#def terminal_disp():

#def change_password():
