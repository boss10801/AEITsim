from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

filename = './yourKey/AESkey.txt'

# open Original file in binary mode
with open(filename, 'rb') as org_file:
    org_data = org_file.read()

# get the public key filename directly from the same directory
pub_pem = './foreignKey/pub.pem'

with open(pub_pem, 'rb') as pub_key_file:
    # De-serialize it back to an object  in public key
    public_key = serialization.load_pem_public_key(
        pub_key_file.read()
    )


encrypted = public_key.encrypt(
    org_data,
    padding.OAEP( #Optimal Asymmetric Encryption padding should be used in RSA Encryption
    #mask generation function (mgf) produce a mask that associated with the size of the input data
    #hashes.SHA256() produce a hash to check that sent massage is
    #unaltered but in itself is of fixed size(256 bits)

    mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(),
    label=None
    )
)

with open(filename+'.encrypted','wb') as file:
    file.write(encrypted) #DAta
