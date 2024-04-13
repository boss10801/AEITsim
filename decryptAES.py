from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
# Take key and initialize vector from another user
AESkey = './yourKey/AESkey.txt'
# initVector = './yourKey/iv.txt'
initVector = './foreignKey/iv.txt'

# Read the Key and IV from yourKey folder
with open(AESkey, 'r') as key_file:
    key_hex = key_file.read()
AESkey = bytes.fromhex(key_hex)     # Convert hex

with open(initVector, 'r') as iv_file:
    iv_hex = iv_file.read()
initVector = bytes.fromhex(iv_hex)  # Convert hex


# Create a Decryptor for AES algorithm, and CBC mode
cipher = Cipher(algorithms.AES(AESkey), modes.CBC(initVector))
decryptor = cipher.decryptor()

# Read the encrypted data
with open('data.txt.encrypted', 'rb') as file:
    ciphertext = file.read()

#First: Decrypt the data
padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
#Second: Unpadding data
unpadder = padding.PKCS7(128).unpadder()
plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

# Write the decrypted data back to a file
with open('data.txt.decrypted', 'wb') as file:
    file.write(plaintext)