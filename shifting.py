def sumroll():
    rollnumber = input("enter the roll number: ")
    sum=0
    for i in rollnumber:
        sum += int(i)
    return sum
def encryption(text, shift):
    result = ''
    for char in text:
        if char.isalpha():

            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result
name = "Amarnath"
shift = sumroll()
cyphername = encryption(name, shift)
print("Encrypted Name:", cyphername)
