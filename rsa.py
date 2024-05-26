import math

def gcd(a, h):
    while h != 0:
        a, h = h, a % h
    return a

def generate_rsa_keys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2

    while True:
        if gcd(e, phi) == 1:
            break
        e += 1

    k = 2
    while True:
        d = (1 + (k * phi)) // e
        if (d * e) % phi == 1:
            break
        k += 1

    return (e, n), (d, n)

def text_to_binary(text):
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    return binary_string

def binary_to_text(binary_string):
    text = ''.join(chr(int(binary_string[i:i + 8], 2)) for i in range(0, len(binary_string), 8))
    return text

def rsa_encrypt(binary_string, public_key):
    e, n = public_key
    N = n.bit_length()
    block_size = N - 2
    ciphertext_blocks = []

    for i in range(0, len(binary_string), block_size):
        block = binary_string[i:i+block_size]
        block_int = int(block, 2)
        encrypted_block = pow(block_int, e, n)
        ciphertext_blocks.append(format(encrypted_block, '0{}b'.format(N)))

    ciphertext_bin = ''.join(ciphertext_blocks)
    return ciphertext_bin

def rsa_decrypt(ciphertext_bin, private_key):
    d, n = private_key
    N = n.bit_length()
    block_size = N
    plaintext_blocks = []

    for i in range(0, len(ciphertext_bin), block_size):
        block = ciphertext_bin[i:i+block_size]
        block_int = int(block, 2)
        decrypted_block = pow(block_int, d, n)
        decrypted_block_binary = format(decrypted_block, '0{}b'.format(N - 2))
        plaintext_blocks.append(decrypted_block_binary)

    binary_plaintext = ''.join(plaintext_blocks)
    return binary_plaintext

# Main demonstration
if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_rsa_keys(p, q)

    # Text to encrypt
    text = "Hello world "
    print(f"Original Text: {text}")

    # Convert text to binary
    binary_string = text_to_binary(text)
    print(f"Original Binary: {binary_string}")

    # Encrypt the binary string
    ciphertext_bin = rsa_encrypt(binary_string, public_key)
    print(f"Ciphertext Binary: {ciphertext_bin}")

    # Decrypt the binary string
    decrypted_bin = rsa_decrypt(ciphertext_bin, private_key)
    print(f"Decrypted Binary: {decrypted_bin}")

    # Convert binary back to text
    decrypted_text = binary_to_text(decrypted_bin)
    print(f"Decrypted Text: {decrypted_text}")
