def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) + shift - shift_base) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text
# Example usage
text = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
print("Encrypted text:", caesar_cipher(text, shift))