
import random
import string

def generate_random_key(length):
    key = ''.join(random.choices(string.ascii_uppercase, k=length))
    return key
def vernam_encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        if message[i].islower():
            base = ord('a')
        else:
            base = ord('A')

        encrypted_char = chr((ord(message[i]) - base + ord(key[i]) - base) % 26 + base)
        #print((ord(message[i]) - base + ord(key[i]) - base) % 26 + base)
        encrypted_message += encrypted_char
    return encrypted_message

def vernam_decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        if encrypted_message[i].islower():
            base = ord('a')
        else:
            base = ord('A')
        decrypted_char = chr((ord(encrypted_message[i]) - base - (ord(key[i]) - base)) % 26 + base)
        decrypted_message += decrypted_char
    return decrypted_message


#message = input("enter the message : ")
message = "helloworld"
length =len(message)
key = generate_random_key(length)

encrypted_message = vernam_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = vernam_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)

