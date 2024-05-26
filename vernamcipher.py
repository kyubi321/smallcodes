
def vernam_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be of equal length.")

    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i]

        # XOR operation and wrapping around the alphabet
        encrypted_char = chr(((ord(char) - ord('a') + ord(key_char) - ord('a')) % 26) + ord('a'))
        ciphertext += encrypted_char

    return ciphertext


def vernam_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Ciphertext and key must be of equal length.")

    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i]

        # XOR operation and wrapping around the alphabet
        decrypted_char = chr(((ord(char) - ord('a') - (ord(key_char) - ord('a'))) % 26) + ord('a'))
        plaintext += decrypted_char

    return plaintext


plaintext = "money"
key = "abcde"
cipher = vernam_encrypt(plaintext, key)
print("Cipher:", cipher)

decrypted_text = vernam_decrypt(cipher, key)
print("Decrypted:", decrypted_text)
