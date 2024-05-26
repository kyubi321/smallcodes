def ecbencrypt(binary): #encyrption for ECB
  ptspace=['000','001','010','011','100','101','110','111'] #plaintext space
  ctspace=['111','110','101','100','011','010','001','000'] #ciphertext space
  cipher = ''
  if (len(binary) % 3 != 0):
    binary += '0' * (3 - len(binary) % 3)
  for i in range(0, len(binary), 3):
    block = binary[i:i+3]
    index = ptspace.index(block)

    cipher += ctspace[index]
  return cipher

def ecbdecrypt(cipher): #decryption for ECB
  ctspace=['000','001','010','011','100','101','110','111'] #ciphertext space
  ptspace=['111','110','101','100','011','010','001','000'] #plaintext space
  plaintext = ""
  if (len(cipher) % 3 != 0):
    binary += '0' * (3 - len(cipher) % 3)
  for i in range(0, len(cipher), 3):
    block = cipher[i:i+3]
    index = ctspace.index(block)
    plaintext += ptspace[index]
  return plaintext

while True:
  print("\nEBC Mode")
  print("1. Encrypt Message")
  print("2. Decrypt Message")
  print("3. Quit")
  choice = input("\nEnter your Choice: ")

  if choice == '1':
    binary = input("Enter the Plaintext: ")
    cipherb= ecbencrypt(binary)
    print("Ciphertext (Binary):", cipherb)
  elif choice == '2':
    cipher = input("Enter the Ciphertext: ")
    plaintext = ecbdecrypt(cipher)
    print("Plaintext (Binary):", plaintext)
  elif choice == '3':
    print("Exiting")
    break
  else:
    print("Invalid choice. Please Enter between 1-3.")