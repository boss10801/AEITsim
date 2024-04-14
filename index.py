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

def copyiv(): #copy from foreignKey to yourKey or from yourKey to foreignKey
    foreignIV = './foreignKey/iv.txt'
    yourIV = './yourKey/iv.txt'

    # Check if iv.txt exists in foreignKey
    if not os.path.exists(foreignIV):
        # If Not, copy it from yourKey
        with open(yourIV, 'r') as iv_file:
            iv_hex = iv_file.read()
        with open(foreignIV, 'w') as iv_file:
            iv_file.write(iv_hex)
    else:
        # If Yes, copy it from foreignKey
        with open(foreignIV, 'r') as iv_file:
            iv_hex = iv_file.read()
        with open(yourIV, 'w') as iv_file:
            iv_file.write(iv_hex)

def main():
    print("Welcome to the AEITsim")
    while True:
        print("Please choose an option:")
        print("1. Key Generation")
        print("2. Encryption")
        print("3. Decryption")
        print("====Only use when key exchange complete====")
        print("4. AES encrypt")
        print("5. AES decrypt")
        print("exit. to exit the program")
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
            encryptionAES()
        elif choice == '5':
            copyiv()
            decryptionAES()
        elif choice == 'exit':
            exit(-1)
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()