# Caesar Cipher – Simple Encryption Tool

A beginner-friendly Python implementation of the **Caesar Cipher**, one of the oldest classical encryption techniques.  
This version supports encryption and decryption of text using any integer shift value, while preserving uppercase, lowercase, and non-alphabetic characters.

---

## Features
- Encrypt and decrypt messages  
- Handles uppercase and lowercase letters  
- Keeps punctuation, numbers, and spaces unchanged  
- Command-line interface (`main.py`)  
- Simple modular design (`cipher.py` handles all logic)

---

## Project Structure
```text
.
├── cipher.py      # Core Caesar Cipher logic
├── main.py        # Command-line tool for user interaction
└── README.md
```

---

## Usage

Run the tool:

```bash
python3 main.py
```

Choose whether to encrypt or decrypt, enter your message, and provide the shift amount.

Example:

```
=== Caesar Cipher Tool ===
1. Encrypt a message
2. Decrypt a message
Select an option (1/2): 1
Enter your message: Hello World!
Enter shift amount (e.g., 3): 5

Encrypted: Mjqqt Btwqi!
```

---

## How It Works
The Caesar Cipher shifts each letter by a chosen amount (e.g., 3 → A→D).  
Non-alphabetic characters remain unchanged.

---

## Project Status
**Status:** ✅ Complete

