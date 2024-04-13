#package requrie: Cryptography
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

#Create a private key
private_key = rsa.generate_private_key(
    # public_exponent use for decode the original data value
    # key_size number of bit used in private key(itself)
    public_exponent = 65537,
    key_size = 2048 
)

# Test key
#print(private_key)

#pem privacy enchand mail
priv_pem = private_key.private_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm = serialization.NoEncryption()
)

# Create a private key in format of byte code
with open('yourKey/priv.pem', 'wb') as priv_pem_file:
    priv_pem_file.write(priv_pem)

#Create a public key
public_key = private_key.public_key()

pub_pem = public_key.public_bytes(
    encoding = serialization.Encoding.PEM,
    format = serialization.PublicFormat.SubjectPublicKeyInfo

)

with open('yourKey/pub.pem', 'wb') as pub_pem_file:
    pub_pem_file.write(pub_pem)