from affine import Affine
from attbash import Attbash
from caesar import Caesar
from kword import Keyword


def encrypt(choice):
    encrypt_input = input("Enter the phrase that you would like encrypted: ")
    print('Your encrypted phrase is ' + choice.encrypt(encrypt_input))


def decrypt(choice):
    decrypt_input = input("Enter the phrase that you would like decrypted: ")
    print('Your decrypted phrase is ' + choice.decrypt(decrypt_input))


def main():
    print("Welcome to Ivan's encrypting / decrypting services!\n")
    user_input = input("Would you like to 'encrypt' or 'decrypt'? Press Q to quit\n").lower()

    if user_input == 'encrypt':
        choice_input = input('''Please select from the following ciphers to encrypt:
    1 - Affine (Ivan special)
    2 - Attbash (Ivan special)
    3 - Caesar (Provided by Treehouse)
    4 - Keyword (Ivan special)\n''')
        if choice_input == '1':
            encrypt(Affine())
        elif choice_input == '2':
            encrypt(Attbash())
        elif choice_input == '3':
            encrypt(Caesar())
        elif choice_input == '4':
            encrypt(Keyword())

    elif user_input == 'decrypt':
        choice_input = input('''Please select from the following ciphers to decrypt:
    1 - Affine (Ivan special)
    2 - Attbash (Ivan special)
    3 - Caesar (Provided by Treehouse)
    4 - Keyword (Ivan special)\n''')
        if choice_input == '1':
            decrypt(Affine())
        elif choice_input == '2':
            decrypt(Attbash())
        elif choice_input == '3':
            decrypt(Caesar())
        elif choice_input == '4':
            decrypt(Keyword())


if __name__ == "__main__":
    main()
