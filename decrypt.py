from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

import sys

filename = './yourKey/AESkey.txt'

# Open the encrypted file in binary mode
with open(filename+'.encrypted', 'rb') as encrypt_file:
    encrypted = encrypt_file.read()

# get the private key filename directly from the same directory
priv_pem = './yourKey/priv.pem'

with open(priv_pem, 'rb') as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None
    )


decrypted = private_key.decrypt(
    encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

with open(filename+'.decrypted', 'wb') as file:
    file.write(decrypted)