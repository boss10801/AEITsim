import os

def key_generation():
    os.system('python gen_keys.py')
    os.system('python gen_keysAES.py')

def encryption():
    filename = input("Enter the name of the file you want to encrypt: ")
    os.system(f'python encrypt.py {filename}')
    os.system(f'python encryptAES.py {filename}')

def decryption():
    os.system('python decrypt.py')
    os.system('python decryptAES.py')

def main():
    print("Welcome to the Encryption/Decryption Program!")
    print("Please choose an option:")
    print("1. Key Generation")
    print("2. Encryption")
    print("3. Decryption")
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        key_generation()
    elif choice == '2':
        encryption()
    elif choice == '3':
        decryption()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()