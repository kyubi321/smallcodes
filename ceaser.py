def encryption(text):
    result = ''
    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted_char = chr((ord(char) - start + 3) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result


def decryption(text):
    result = ''
    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted_char = chr((ord(char) - start - 3) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result

name = "Amarnath"
cyphername = encryption(name)
decrypted_text = decryption(cyphername)
print("Encrypted Name:", cyphername)
print("Decrypted Name:", decrypted_text)