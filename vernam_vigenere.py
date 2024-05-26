def encrypt(plaintext,key):
    ciphertext=""
    for i in range(len(plaintext)):
        char = plaintext[i]
        if char.isalpha():
            if char.isupper():
                start=ord('A')
            else:
                start=ord('a')
            key = key[i % len(key)]
            encrypted_char = chr((ord(char) - start+ ord(key)) % 26 + start)
            ciphertext+= encrypted_char
    return ciphertext


def decrypt(ciphertext,key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        if char.isalpha():
            if char.isupper():
                start=ord('A')
            else:
                start=ord('a')
            key = key[i % len(key)]
            decrypted_char = chr((ord(char) - start - ord(key)) % 26 + start)
            plaintext+= decrypted_char
    return plaintext
plaintext = "superman is op"
key = "batman"
ciphertext = encrypt(plaintext,key)
decryptedtext= decrypt(ciphertext,key)
print(f"Encrypted Ciphertext: {ciphertext}")
print(f"Decrypted Plaintext: {decryptedtext}")
