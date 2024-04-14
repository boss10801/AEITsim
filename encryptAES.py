import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding

# Take key and initialize vector from another user
AESkey = './yourKey/AESkey.txt'
initVector = './yourKey/iv.txt'

# Read the Key and IV from yourKey folder
with open(AESkey, 'r') as key_file:
    key_hex = key_file.read()
AESkey = bytes.fromhex(key_hex)     # Convert hex

with open(initVector, 'r') as iv_file:
    iv_hex = iv_file.read()
initVector = bytes.fromhex(iv_hex)  # Convert hex

# Create a Encryptor with AES algorithm, and CBC mode
cipher = Cipher(algorithms.AES(AESkey), modes.CBC(initVector))
padder = padding.PKCS7(128).padder()    # Padding before encrypt

# Read data from the file
filename = sys.argv[1]
with open(filename, 'rb') as file:
    plaintext = file.read()

#First: Padding data
padded_data = padder.update(plaintext) + padder.finalize()
#Second: Encrypt the data
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Write the encrypted data back to a file
with open(f'{filename}.encrypted', 'wb') as file:
    file.write(ciphertext)