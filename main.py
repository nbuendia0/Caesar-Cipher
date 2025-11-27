# main.py
# Basic command-line interface for the Caesar Cipher project

from cipher import encrypt, decrypt

def main():
    print("=== Caesar Cipher Tool ===")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    choice = input("Select an option (1/2): ").strip()

    if choice not in ("1", "2"):
        print("Invalid selection.")
        return

    message = input("Enter your message: ").strip()

    try:
        shift = int(input("Enter shift amount (e.g., 3): ").strip())
    except ValueError:
        print("Shift must be a number.")
        return

    if choice == "1":
        output = encrypt(message, shift)
        print(f"\nEncrypted: {output}")
    else:
        output = decrypt(message, shift)
        print(f"\nDecrypted: {output}")


if __name__ == "__main__":
    main()
