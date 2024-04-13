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

# Create a Cipher object with the key, AES algorithm, and CBC mode
cipher = Cipher(algorithms.AES(AESkey), modes.CBC(initVector))
# Create a padder object
padder = padding.PKCS7(128).padder()

# Read data from the file
with open('data.txt', 'rb') as file:
    plaintext = file.read()
padded_data = padder.update(plaintext) + padder.finalize()

# Encrypt the data
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded_data) + encryptor.finalize()

# Write the encrypted data back to a file
with open('data.txt.encrypted', 'wb') as file:
    file.write(ciphertext)