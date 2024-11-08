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
        """Encode the input string using random shifts, with shift values embedded.
        The output is then converted to hexadecimal."""
        encoded_chars = []

        for char in data:
            shift = random.randint(self.min_shift, self.max_shift)
            shifted_char = chr((ord(char) + shift) % 256)  # Shift the character
            # Convert the shifted character to its hexadecimal representation
            hex_shift = format(shift, 'x')  # Convert shift value to hex
            hex_char = format(ord(shifted_char), 'x')  # Convert the shifted character to hex
            encoded_chars.append(f"{hex_shift}{hex_char}")  # Combine the shift and the hex character

        encoded_string = ''.join(encoded_chars)
        return encoded_string

    def decode(self, encoded_data):
        """Decode the encoded string by reversing the embedded shifts from hexadecimal."""
        decoded_chars = []
        i = 0

        while i < len(encoded_data):
            # Read the shift (2 hex characters) and the encoded character (2 hex characters)
            shift = int(encoded_data[i:i+2], 16)  # Convert shift from hex to int
            shifted_char_hex = encoded_data[i+2:i+4]
            shifted_char = chr(int(shifted_char_hex, 16))  # Convert the hex char back to character
            original_char = chr((ord(shifted_char) - shift) % 256)  # Reverse the shift to get original
            decoded_chars.append(original_char)
            i += 4  # Move to the next set of shift and encoded character (each is 2 hex chars)

        decoded_string = ''.join(decoded_chars)
        return decoded_string

# Create a default instance of Dexter
_default_dexter = Dexter()

# Expose encode and decode as module-level functions
encode = _default_dexter.encode
decode = _default_dexter.decode
    
