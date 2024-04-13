import secrets

# Generate a random 256-bit key and 128-bit Initialization Vector
key = secrets.token_bytes(32)
initVector = secrets.token_bytes(16)

key_hex = key.hex()
iv_hex = initVector.hex()

# Write the key to a file
with open('yourKey/AESkey.txt', 'w') as key_file:
    key_file.write(key_hex)

# Write the IV to a file
with open('yourKey/iv.txt', 'w') as iv_file:
    iv_file.write(iv_hex)