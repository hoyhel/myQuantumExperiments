import random
import string

class Cipher:

    def __init__(self, key=''.join(random.choice(string.ascii_lowercase) for _ in range(100))):
        self.key = key
        self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                         't', 'u', 'v', 'w', 'x', 'y', 'z']

    def encode(self, text):
        new_text = ""
        for index, char in enumerate(text):
            index_for_key = index % len(self.key)
            key = self.key[index_for_key]
            key_index = self.alphabet.index(key)
            char_index = (self.alphabet.index(char) + key_index) % len(self.alphabet)
            new_char = self.alphabet[char_index]
            new_text += new_char
        return new_text

    def decode(self, text):
        # Reverse of encode
        new_text = ""
        for index, char in enumerate(text):
            index_for_key = index % len(self.key)
            key = self.key[index_for_key]
            key_index = self.alphabet.index(key)
            char_index = (self.alphabet.index(char) - key_index) % len(self.alphabet)
            new_char = self.alphabet[char_index]
            new_text += new_char
        return new_text