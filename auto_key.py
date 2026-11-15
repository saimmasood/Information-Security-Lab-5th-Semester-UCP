def encrypt_autokey(plaintext, key):
    plaintext = ''.join(
        char.upper() for char in plaintext if char.isalpha()
    )

    key = ''.join(
        char.upper() for char in key if char.isalpha()
    )

    # Generate key stream
    keystream = key

    while len(keystream) < len(plaintext):
        keystream += plaintext

    # Make sure key stream is exactly the plaintext length
    keystream = keystream[:len(plaintext)]

    ciphertext = ""

    for i in range(len(plaintext)):

        p = ord(plaintext[i]) - ord('A')
        k = ord(keystream[i]) - ord('A')

        c = (p + k) % 26

        ciphertext += chr(c + ord('A'))

    return ciphertext, keystream


def decrypt_autokey(ciphertext, key):
    ciphertext = ''.join(
        char.upper() for char in ciphertext if char.isalpha()
    )

    key = ''.join(
        char.upper() for char in key if char.isalpha()
    )

    plaintext = ""

    for i in range(len(ciphertext)):

        # Initial keyword
        if i < len(key):
            k = ord(key[i]) - ord('A')

        # Previously recovered plaintext
        else:
            k = ord(plaintext[i - len(key)]) - ord('A')

        c = ord(ciphertext[i]) - ord('A')

        p = (c - k) % 26

        plaintext += chr(p + ord('A'))

    return plaintext


# Main program
plaintext = input("Enter plaintext: ")
key = input("Enter initial keyword: ")

ciphertext, keystream = encrypt_autokey(plaintext, key)

print("\nGenerated Key Stream:", keystream)
print("Ciphertext:", ciphertext)

decrypted = decrypt_autokey(ciphertext, key)

print("Decrypted text:", decrypted)























# def encrypt_autokey(plaintext, key):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     plaintext = plaintext.upper()
#     key = key.upper()

#     result = ""

#     keystream = key

#     while len(keystream) < len(plaintext):
#         keystream = keystream + plaintext

#     keystream = keystream[:len(plaintext)]

#     for i in range(len(plaintext)):
#         p = alphabet.index(plaintext[i])
#         k = alphabet.index(keystream[i])

#         c = (p + k) % 26

#         result = result + alphabet[c]

#     return result, keystream


# def decrypt_autokey(ciphertext, key):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#     ciphertext = ciphertext.upper()
#     key = key.upper()

#     result = ""

#     for i in range(len(ciphertext)):
#         if i < len(key):
#             k = alphabet.index(key[i])
#         else:
#             k = alphabet.index(result[i - len(key)])

#         c = alphabet.index(ciphertext[i])
#         p = (c - k) % 26

#         result = result + alphabet[p]

#     return result


# plaintext = input("Enter plaintext: ")
# key = input("Enter initial keyword: ")

# ciphertext, keystream = encrypt_autokey(plaintext, key)

# print("Generated Key Stream:", keystream)
# print("Ciphertext:", ciphertext)

# decrypted = decrypt_autokey(ciphertext, key)

# print("Decrypted text:", decrypted)




























def encrypt_autokey(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = key.upper()
    clean_key = ""

    for char in key:
        if char in alphabet:
            clean_key = clean_key + char

    if clean_key == "":
        raise ValueError("Keyword must contain an English letter.")

    clean_text = ""
    for char in plaintext:
        if char.upper() in alphabet:
            clean_text = clean_text + char.upper()

    keystream = clean_key

    while len(keystream) < len(clean_text):
        keystream = keystream + clean_text

    keystream = keystream[:len(clean_text)]

    result = ""
    key_index = 0

    for char in plaintext:
        if char.upper() in alphabet:
            p = alphabet.index(char.upper())
            k = alphabet.index(keystream[key_index])

            c = (p + k) % 26
            result = result + alphabet[c]

            key_index = key_index + 1
        else:
            result = result + char

    return result


def decrypt_autokey(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    key = key.upper()
    clean_key = ""

    for char in key:
        if char in alphabet:
            clean_key = clean_key + char

    if clean_key == "":
        raise ValueError("Keyword must contain an English letter.")

    result = ""
    result_letters = ""
    key_index = 0

    for char in ciphertext:
        if char.upper() in alphabet:
            c = alphabet.index(char.upper())

            if key_index < len(clean_key):
                k = alphabet.index(clean_key[key_index])
            else:
                k = alphabet.index(
                    result_letters[key_index - len(clean_key)]
                )

            p = (c - k) % 26
            letter = alphabet[p]

            result = result + letter
            result_letters = result_letters + letter

            key_index = key_index + 1
        else:
            result = result + char

    return result


plaintext = input("Enter plaintext: ")
key = input("Enter keyword: ")

ciphertext = encrypt_autokey(plaintext, key)
print("\nCiphertext:", ciphertext)

decrypted = decrypt_autokey(ciphertext, key)
print("Decrypted text:", decrypted)
