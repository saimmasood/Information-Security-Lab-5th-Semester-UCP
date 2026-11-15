def encrypt_caesar(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            encrypted = chr((ord(char) - base + key) % 26 + base)

            result += encrypted
        else:
            result += char

    return result


def decrypt_caesar(text, key):
    return encrypt_caesar(text, -key)


# Main program
plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

ciphertext = encrypt_caesar(plaintext, key)
decrypted = decrypt_caesar(ciphertext, key)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)





def encrypt_caesar(text, key):
    result = ""

    for x in text:
        if x.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"

            if x.isupper():
                alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

            old_position = alphabet.index(x)
            new_position = (old_position + key) % 26

            result = result + alphabet[new_position]
        else:
            result = result + x

    return result


def decrypt_caesar(text, key):
    return encrypt_caesar(text, -key)


plaintext = input("Enter plaintext: ")
key = int(input("Enter key: "))

ciphertext = encrypt_caesar(plaintext, key)
decrypted = decrypt_caesar(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)




