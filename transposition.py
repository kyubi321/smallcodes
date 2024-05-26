
def encrypt(plaintext, keyword):
    try:

        plaintext = plaintext.replace(" ", "").upper()
        keyword = keyword.upper()
        num_columns = len(keyword)

        column_order = {char: i for i, char in enumerate(sorted(keyword))}

        """finding the number of rows"""
        num_rows = -(-(len(plaintext) // num_columns))

        """ making the grid for arranging the letters"""

        grid = []
        for _ in range(num_rows):
            grid.append([""] * num_columns)


        for i, char in enumerate(plaintext):
            row_index = i // num_columns
            col_index = column_order[keyword[i % num_columns]]
            grid[row_index][col_index] = char


        ciphertext = ""
        for row in grid:
            ciphertext += "".join(row)

        return ciphertext
    except:
        print("the key is not compatible")


def decrypt(ciphertext, keyword):
    try:

        ciphertext = ciphertext.replace(" ", "").upper()
        keyword = keyword.upper()
        num_columns = len(keyword)

        column_order = {char: i for i, char in enumerate(sorted(keyword))}

        """finding the number of rows"""
        num_rows = -(-(len(ciphertext) // num_columns))

        """ making the grid for arranging the letters"""

        grid = []
        for _ in range(num_rows):
            grid.append([""] * num_columns)


        for i, char in enumerate(ciphertext):
            row_index = i // num_columns
            col_index = column_order[keyword[i % num_columns]]
            grid[row_index][col_index] = char


        plaintext = ""
        for row in grid:
            plaintext += "".join(row)

        return plaintext
    except:
        print("the key is not compatible")


plaintext = "attack at the dawn"
key = "lemon"
cipher = encrypt(plaintext, key)
print("Encrypted Plaintext:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted Plaintext:", decrypted)
