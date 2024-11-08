# Dexter Encoder

`Dexter` is a custom encoding library that obfuscates shellcode for security testing purposes. It uses complex encoding rules to avoid detection by IDS.

## Installation

You can install Dexter via pip:

```bash
pip install dexter-encoder


import dexter as d  # Import the Dexter encoding library

# Sample data to encode
data = "this is secret data"

# Encode the data
encoded_data = d.encode(data)
print(f"Encoded: {encoded_data}")

# Decode the data back to original
decoded_data = d.decode(encoded_data)
print(f"Decoded: {decoded_data}")

Encoded: "1a<shifted chars>bc"
Decoded: "this is secret data"
