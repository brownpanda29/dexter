# dexter.py

import random

class Dexter:
    def __init__(self, min_shift=10, max_shift=50):
        """
        Initialize Dexter encoding with a specified shift range.
        Args:
            min_shift (int): Minimum shift value for encoding.
            max_shift (int): Maximum shift value for encoding.
        """
        self.min_shift = min_shift
        self.max_shift = max_shift

    def encode(self, data):
        """Encode the input string using random shifts, with shift values embedded."""
        encoded_chars = []

        for char in data:
            shift = random.randint(self.min_shift, self.max_shift)
            shifted_char = chr((ord(char) + shift) % 256)
            encoded_chars.append(f"{chr(shift)}{shifted_char}")

        encoded_string = ''.join(encoded_chars)
        return encoded_string

    def decode(self, encoded_data):
        """Decode the encoded string by reversing the embedded shifts."""
        decoded_chars = []
        i = 0

        while i < len(encoded_data):
            shift = ord(encoded_data[i])
            shifted_char = encoded_data[i + 1]
            original_char = chr((ord(shifted_char) - shift) % 256)
            decoded_chars.append(original_char)
            i += 2

        decoded_string = ''.join(decoded_chars)
        return decoded_string

# Create a default instance of Dexter
_default_dexter = Dexter()

# Expose encode and decode as module-level functions
encode = _default_dexter.encode
decode = _default_dexter.decode
