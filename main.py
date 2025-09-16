import sys

def caesar_cipher(msg: str, shift: int) -> str:
    result = ''

    for char in msg:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            offset = (ord(char) - start + shift) % 26
            result += chr(start + offset)
        else:
            result += char

    return result

def opplok_cipher(msg: str, shift: int) -> str:
    result = ''

    for char in msg:
        if char.isalpha():
            result += caesar_cipher(char, ord(char) + shift)
        else:
            result += char

    return result


def encrypt_demo():
    print("Encryption")
    message = input("Enter message: ")
    shift = 3
    encrypted = caesar_cipher(message, shift)
    print(f"Encrypted message: {encrypted}")

def dencrypt_demo():
    print("Decryption")
    message = input("Enter message: ")
    shift = -3
    encrypted = caesar_cipher(message, shift)
    print(f"Decrypted message: {encrypted}")

def brute_force_demo():
    print("Brute-Force")
    message = input("Enter message: ")
    for i in range(1, 26):
        encrypted = caesar_cipher(message, i)
        print(f"Shift {i}: {encrypted}")

def opplok_encrypt_demo():
    print("Opplok Encryption")
    message = input("Enter message: ")
    shift = 3
    encrypted = opplok_cipher(message, shift)
    print(f"Encrypted message: {encrypted}")

def menu():
    options = {
        '1': ("Encrypt (Shift +3)", lambda: encrypt_demo()),
        '2': ("Dencrypt (Shift -3)", lambda: dencrypt_demo()),
        '3': ("Brute-force decode (try all shifts)", lambda: brute_force_demo()),
        '4': ("Opplok Encrypt (Shift +3)", lambda: opplok_encrypt_demo()),
        '0': ("Exit", lambda : sys.exit()),
    }
    while True:
        print()
        print("Caesar Cipher Activity")
        for num, (text, _func) in options.items():
            print(f"{num}.) {text}")
        choose = input("Choose an options (1-4): ")
        action = options.get(choose)
        if action:
            print()
            action[1]()

if __name__ == "__main__":
    menu()