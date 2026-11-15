def encrypt_vigenere(plaintext, key):
    result = ""
    key = key.upper()

    key_index = 0

    for char in plaintext:
        if char.isalpha():

            p = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            encrypted = chr((p + k) % 26 + ord('A'))

            result += encrypted

            key_index += 1

        else:
            result += char

    return result


def decrypt_vigenere(ciphertext, key):
    result = ""
    key = key.upper()

    key_index = 0

    for char in ciphertext:
        if char.isalpha():

            c = ord(char.upper()) - ord('A')
            k = ord(key[key_index % len(key)]) - ord('A')

            decrypted = chr((c - k) % 26 + ord('A'))

            result += decrypted

            key_index += 1

        else:
            result += char

    return result


# Main program
plaintext = input("Enter plaintext: ")
key = input("Enter keyword: ")

ciphertext = encrypt_vigenere(plaintext, key)
decrypted = decrypt_vigenere(ciphertext, key)

print("\nCiphertext:", ciphertext)
print("Decrypted text:", decrypted)

















def encrypt_vigenere(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key = key.upper()
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            letter = char.upper()

            p = alphabet.index(letter)
            k = alphabet.index(key[key_index % len(key)])

            new_position = (p + k) % 26
            result = result + alphabet[new_position]

            key_index = key_index + 1
        else:
            result = result + char

    return result


def decrypt_vigenere(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    key = key.upper()
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            letter = char.upper()

            c = alphabet.index(letter)
            k = alphabet.index(key[key_index % len(key)])

            new_position = (c - k) % 26
            result = result + alphabet[new_position]

            key_index = key_index + 1
        else:
            result = result + char

    return result


plaintext = input("Enter plaintext: ")
key = input("Enter keyword: ")


ciphertext = encrypt_vigenere(plaintext, key)
decrypted = decrypt_vigenere(ciphertext, key)

print("Ciphertext:", ciphertext)
print("Decrypted text:", decrypted)






def encrypt_vg(plain,k):
    plain=plain.upper()
    k=k.upper()

    alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    result=""
    k_index=0

    for char in plain:
        if char.alpha():
            p=alphabets.index(char)
            k=alphabets.index(k[k_index % len(k)])

            c=(k+p)%26
            result=result+alphabets[c]
            k_index= k_index+1
        else :
            result=result+char
    return result
