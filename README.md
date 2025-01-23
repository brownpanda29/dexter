

---

# Dexter Encoder

Dexter is a custom encoding library designed for security professionals and developers who need to obfuscate shellcode or sensitive data as part of security testing and analysis. By applying complex encoding rules, Dexter aims to bypass Intrusion Detection Systems (IDS) and evade signature-based detection, making it a valuable tool in controlled, ethical hacking and red team assessments.  

## Features
- **Advanced Encoding**: Uses dynamic, randomized shifts to obfuscate data effectively.
- **Simple Interface**: Easy-to-use `encode()` and `decode()` methods for quick encoding and decoding.
- **Security-Oriented**: Designed to enhance security testing workflows while minimizing the risk of detection.

## Installation

Install Dexter easily via pip:                          
```bash
pip install dexter-encoder
```

## Usage

Once installed, you can import the Dexter library and use the `encode()` and `decode()` methods to obfuscate and deobfuscate your data.

### Example:

```python
import dexter as d  # Import the Dexter encoding library
```

### Encoding & Decoding
```python
data = "this is secret data"

# Encoding the data
encoded_data = d.encode(data)
print(f"Encoded: {encoded_data}")

# Decoding the data
decoded_data = d.decode(encoded_data)
print(f"Decoded: {decoded_data}")
```

---

## Handling Problematic Inputs

Some inputs can cause issues when directly processed by the Dexter encoder due to their unique encoding properties. These problematic inputs include:

| Input                       | Description                  |
|-----------------------------|------------------------------|
| `𝒜𝓂𝑜𝑔𝒾`                  | Unicode characters           |
| `😀😁😂🤣😃😄😅😆`          | Emojis                       |
| `Привет мир`                | Non-Latin characters (Russian) |
| `مرحبا بالعالم`           | Arabic script                |
| `こんにちは世界`           | Japanese script              |
| `你好，世界`                | Chinese script               |
| `⁰¹²³⁴⁵⁶⁷⁸⁹`               | Superscript numbers          |
| `₀₁₂₃₄₅₆₇₈₉`               | Subscript numbers            |
| `©®™✓✗✠✡`                  | Symbols                      |
| `👩‍👩‍👦‍👦`                  | Complex emoji (family)       |
| `\ud83d\ude02`              | Isolated surrogate pair      |

### Mitigation Strategy

To handle these inputs effectively, follow this process:
1. **Base64 Encode the Input**: Convert the problematic input into a base64-encoded string. This ensures that any special characters or symbols are safely represented.
2. **Use Dexter**: Pass the base64-encoded string through the Dexter encoder to apply obfuscation.

#### Example:
```python
import base64
import dexter as d

# Problematic input
data = "😀😁😂🤣😃😄😅😆"

# Step 1: Base64 encode the data
base64_data = base64.b64encode(data.encode()).decode()

# Step 2: Encode with Dexter
encoded_data = d.encode(base64_data)
print(f"Encoded: {encoded_data}")

# To decode:
decoded_base64 = d.decode(encoded_data)
original_data = base64.b64decode(decoded_base64.encode()).decode()
print(f"Original: {original_data}")
```

### Note from the Author

As the author of Dexter, I haven't yet figured out a way to mitigate this issue directly in the encoder itself. For now, the solution is to first base64 encode the inputs before using Dexter. I am actively working on resolving this limitation in future updates.
