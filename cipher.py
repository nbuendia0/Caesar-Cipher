# cipher.py
# Simple Caesar Cipher implementation (original code, not based on any external repo)

def encrypt(text: str, shift: int) -> str:
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    return encrypt(text, -shift)
