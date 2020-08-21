from secrets import token_bytes

"""
The one time pad is an unbreakable encryption.
A random function is used to generate a one time key that
is the same length with the data to encrypt. The data is
XORed with the key to produce an encryption.
Decryption is done by XORing the encryption with the key.
"""

def random_key(length):
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original):
    original_bytes = original.encode()
    # To make sure the key and data are the same num of bytes
    key = random_key(len(original_bytes))
    # bitstring is needed to xor
    original_bitsring = int.from_bytes(original_bytes, "big")
    # XOR (^) automatically converts ints to binary and back
    encrypted = original_bitsring ^ key
    return key, encrypted

def decrypt(encrypted, key):
    original_bitstring = encrypted ^ key
    original_bytes = int.to_bytes(original_bitstring, (encrypted.bit_length() + 7)//8, "big")
    original = original_bytes.decode()
    return original

if __name__ == "__main__":
    key, encryption = encrypt(input("Enter text to be encrypted:\n"))
    print(f"Here is your one-time-key: \n{key}")
    print(f"and your encryped message: \n{encryption}")
