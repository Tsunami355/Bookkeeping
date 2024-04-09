def decrypt(encrypted_message, key):
    result = ""
    for char in encrypted_message:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - shift - key) % 26 + shift)
            result += decrypted_char
        else:
            result += char
    return result


if __name__ == "__main__":
    key = int(input("Enter key: "))
    encrypted_message = input("Enter an encrypted message: ")
    decrypted_message = decrypt(encrypted_message, key)
    print(f"Результат: {decrypted_message}")
