from ciphers import Cipher


class Keyword(Cipher):

    my_dict = {
        'A': 'K', 'B': 'R', 'C': 'Y', 'D': 'P', 'E': 'T',
        'F': 'O', 'G': 'S', 'H': 'A', 'I': 'B', 'J': 'C',
        'K': 'D', 'L': 'E', 'M': 'F', 'N': 'G', 'O': 'H',
        'P': 'I', 'Q': 'J', 'R': 'L', 'S': 'M', 'T': 'N',
        'U': 'Q', 'V': 'U', 'W': 'V', 'X': 'W', 'Y': 'X',
        'Z': 'Z', ' ': ' '
    }

    def __init__(self):
        self.my_dict

    def encrypt(self, text):
        """This method encrypts using keyword cipher"""
        text = text.upper()
        encrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == key:
                    encrypted_list.append(value)
        return ''.join(encrypted_list)

    def decrypt(self, text):
        """This method decrypts using keyword cipher"""
        text = text.upper()
        decrypted_list = []
        for char in text:
            for key, value in self.my_dict.items():
                if char == value:
                    decrypted_list.append(key)
        return ''.join(decrypted_list)


# print(Keyword().encrypt('Knowledge is power'))
# print(Keyword().decrypt('DGHVETPST BM IHVTL'))