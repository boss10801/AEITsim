from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets

# Create a random 256-bit key
key = secrets.token_bytes(32)

# Create a random 128-bit Initialization Vector
initVector = secrets.token_bytes(16)

# Cipher object with the key, AES algorithm, and CBC mode
cipher = Cipher(algorithms.AES(key), modes.CBC(initVector))

# Create an encryptor object
encryptor = cipher.encryptor()

# Encrypt Test data
plaintext = b"a secret message"
ciphertext = encryptor.update(plaintext) + encryptor.finalize()

# Decrypt Test data
# Create a new Cipher object because the last one is died
cipher = Cipher(algorithms.AES(key), modes.CBC(initVector))
decryptor = cipher.decryptor()
decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

print(decrypted_text)  # Outputs: b'a secret message'
