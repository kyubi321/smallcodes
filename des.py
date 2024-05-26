
sbox = [
    [2, 15, 3, 14, 4, 13, 5, 12, 6, 11, 7, 10, 8, 1, 9, 0],
    [0, 8, 15, 7, 14, 6, 13, 5, 12, 4, 11, 3, 10, 2, 9, 1],
    [4, 8, 14, 6, 1, 10, 5, 13, 15, 9, 3, 12, 0, 7, 11, 2],
    [6, 12, 7, 13, 0, 14, 1, 15, 2, 11, 3, 10, 4, 9, 5, 8]
]

def to_bits(message):
    bits = ''
    for c in message:
        bits += format(ord(c), '08b')
    return bits

def from_bits(bits):
    message = ''
    for i in range(0, len(bits), 8):
        message += chr(int(bits[i:i+8], 2))
    return message

def permutation(binary, table):
    return ''.join(binary[i - 1] for row in table for i in row)

def xor(bin1, bin2):
    return ''.join('1' if a != b else '0' for a, b in zip(bin1, bin2))

def sbox_substitution(binary, sbox):
    row = int(binary[0] + binary[5], 2)
    col = int(binary[1:5], 2)
    return sbox[row][col]


sbox = [list(row) for row in sbox]


def encrypt(plaintext, key):
    pb = to_bits(plaintext)[:16]
    p = permutation(pb, initial_permutation_table)
    lo, ro = p[:8], p[8:]  # Left and right halves
    er = permutation(ro, expansion_permutation_table)
    ex = xor(er, key[:12])
    lh, rh = ex[:6], ex[6:]
    sl, sr = sbox_substitution(lh, sbox[0]), sbox_substitution(rh, sbox[1])
    sc = sl + sr
    ps = permutation(sc, final_permutation_table)
    r1 = xor(ps, lo)
    l1 = ro
    return permutation(l1 + r1, [inverse_initial_permutation_table[i] for i in range(4)])

def decrypt(ciphertext, key):
    p = permutation(ciphertext, inverse_initial_permutation_table)
    lo, ro = p[:8], p[8:]  # Left and right halves
    er = permutation(ro, expansion_permutation_table)
    ex = xor(er, key[:12])
    lh, rh = ex[:6], ex[6:]
    sl, sr = sbox_substitution(lh, sbox[0]), sbox_substitution(rh, sbox[1])
    sc = sl + sr
    ps = permutation(sc, final_permutation_table)
    r0 = xor(ps, lo)
    l0 = ro
    return ''.join(chr(int(permutation(l0 + r0, [initial_permutation_table[i] for i in range(4)])[i:i+8], 2)) for i in range(0, 16, 8))

# S-boxes

# Permutation tables
initial_permutation_table = [
    [1, 12, 9, 5],
    [13, 2, 6, 10],
    [15, 11, 3, 14],
    [16, 7, 8, 4]
]

expansion_permutation_table = [
    [8, 1, 2, 3, 4, 5],
    [4, 5, 6, 7, 8, 1]
]

final_permutation_table = [
    [4, 1, 2, 3],
    [7, 8, 6, 5]
]

inverse_initial_permutation_table = [
    [4, 8, 12, 16],
    [3, 7, 11, 15],
    [2, 6, 10, 14],
    [1, 5, 9, 13]
]

# Test
plaintext = "HELLO"
key = "100110111010"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")