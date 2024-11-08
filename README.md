# Dexter Encoder

`Dexter` is a custom encoding library that obfuscates shellcode for security testing purposes. It uses complex encoding rules to avoid detection by IDS.

## Installation

You can install Dexter via pip:

```bash
pip install dexter-encoder 
```

## Usage

Once installed, you can import the Dexter library and use the `encode()` and `decode()` methods to obfuscate and deobfuscate your data.

### Example:

```python
import dexter as d  # Import the Dexter encoding library
```

# Sample data to encode
data = "this is secret data"

# Encode the data
encoded_data = d.encode(data)
print(f"Encoded: {encoded_data}")

# Decode the data back to original
decoded_data = d.decode(encoded_data)
print(f"Decoded: {decoded_data}")
