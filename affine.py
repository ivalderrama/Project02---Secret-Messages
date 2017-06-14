from ciphers import Cipher


class Affine(Cipher):

    my_dict = {
        'A': 'I', 'B': 'N', 'C': 'S', 'D': 'X', 'E': 'C',
        'F': 'H', 'G': 'M', 'H': 'R', 'I': 'W', 'J': 'B',
        'K': 'G', 'L': 'L', 'M': 'Q', 'N': 'V', 'O': 'A',
        'P': 'F', 'Q': 'K', 'R': 'P', 'S': 'U', 'T': 'Z',
        'U': 'E', 'V': 'J', 'W': 'O', 'X': 'T', 'Y': 'Y',
        'Z': 'D', ' ': ' '
    }

    def __init__(self):
        self.my_dict

    def encrypt(self, text):
        """This method encrypts using affine cipher"""
        text = text.upper()
        encrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == key:
                    encrypted_list.append(value)
        return ''.join(encrypted_list)

    def decrypt(self, text):
        """This method decrypts using affine cipher"""
        text = text.upper()
        decrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == value:
                    decrypted_list.append(key)
        return ''.join(decrypted_list)


# print(Affine().encrypt('Affine Cipher'))
# print(Affine().decrypt('IHHWVC SWFRCP'))