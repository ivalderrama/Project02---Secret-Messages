from ciphers import Cipher


class Attbash(Cipher):

    my_dict = {
        'A': 'Z', 'B': 'Y', 'C': 'X', 'D': 'W', 'E': 'V',
        'F': 'U', 'G': 'T', 'H': 'S', 'I': 'R', 'J': 'Q',
        'K': 'P', 'L': 'O', 'M': 'N', 'N': 'M', 'O': 'L',
        'P': 'K', 'Q': 'J', 'R': 'I', 'S': 'H', 'T': 'G',
        'U': 'F', 'V': 'E', 'W': 'D', 'X': 'C', 'Y': 'B',
        'Z': 'A', ' ': ' '
    }

    def __init__(self):
        self.my_dict

    def encrypt(self, text):
        """This method encrypts using attbash cipher"""
        text = text.upper()
        encrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == key:
                    encrypted_list.append(value)
        return ''.join(encrypted_list)

    def decrypt(self, text):
        """This method decrypts using attbash cipher"""
        text = text.upper()
        decrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == value:
                    decrypted_list.append(key)
        return ''.join(decrypted_list)


# print(Attbash().encrypt('irk low hob hold holy horn glow'))
# print(Attbash().decrypt('RIP OLD SLY SLOW SLOB SLIM TOLD'))