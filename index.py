import os

def key_generation():
    os.system('python gen_keys.py')
    os.system('python gen_keysAES.py')

def encryption():
    os.system(f'python encrypt.py')

def decryption():
    os.system(f'python decrypt.py')

def encryptionAES():
    filename = input("Enter the name of the file you want to encrypt: ")
    os.system(f'python encryptAES.py {filename}')

def decryptionAES():
    filename = input("Enter the name of the file you want to decrypt: ")
    os.system(f'python decryptAES.py {filename}')

def copyiv(): #copy from foreignKey to yourKey
    initVector = './foreignKey/iv.txt'
    with open(initVector, 'r') as iv_file:
        iv_hex = iv_file.read()
    with open('./yourKey/iv.txt', 'w') as iv_file:
        iv_file.write(iv_hex)

def main():
    print("Welcome to the Encryption/Decryption Program!")
    print("Please choose an option:")
    print("1. Key Generation")
    print("2. Encryption")
    print("3. Decryption")
    print("4. Encryption with AES only")
    print("5. Decryption with AES only")
    print("exit. to exit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        key_generation()
    elif choice == '2':
        encryption()
        encryptionAES()
    elif choice == '3':
        decryption()
        decryptionAES()
    elif choice == '4':
        copyiv()
        # encryptionAES()
    elif choice == '5':
        decryptionAES()
    elif choice == 'exit':
        exit(-1)
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()