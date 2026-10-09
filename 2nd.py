def encrypt_autokey(auto_plaintext, auto_key):
    auto_plaintext = ''.join(
        char.upper() for char in auto_plaintext if char.isalpha()
    )
    auto_key = ''.join(
        char.upper() for char in auto_key if char.isalpha()
    )

    # Generate key stream
    keystream = auto_key
    while len(keystream) < len(auto_plaintext):
        keystream += auto_plaintext

    # Make sure key stream is exactly the plaintext length
    keystream = keystream[:len(auto_plaintext)]
    auto_ciphertext = ""

    for i in range(len(auto_plaintext)):
        p = ord(auto_plaintext[i]) - ord('A')
        k = ord(keystream[i]) - ord('A')
        c = (p + k) % 26
        auto_ciphertext += chr(c + ord('A'))

    return auto_ciphertext, keystream


def decrypt_autokey(auto_ciphertext, auto_key):
    auto_ciphertext = ''.join(
        char.upper() for char in auto_ciphertext if char.isalpha()
    )
    auto_key = ''.join(
        char.upper() for char in auto_key if char.isalpha()
    )

    auto_plaintext = ""

    for i in range(len(auto_ciphertext)):
        # Initial keyword
        if i < len(auto_key):
            k = ord(auto_key[i]) - ord('A')
        # Previously recovered plaintext
        else:
            k = ord(auto_plaintext[i - len(auto_key)]) - ord('A')

        c = ord(auto_ciphertext[i]) - ord('A')
        p = (c - k) % 26
        auto_plaintext += chr(p + ord('A'))

    return auto_plaintext


def encrypt_vigenere(vigenere_plaintext, vigenere_key):
    vigenere_encrypt_result = ""
    vigenere_key = vigenere_key.upper()
    key_index = 0

    for char in vigenere_plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')
            k = ord(vigenere_key[key_index % len(vigenere_key)]) - ord('A')
            vigenere_encrypted = chr((p + k) % 26 + ord('A'))
            vigenere_encrypt_result += vigenere_encrypted
            key_index += 1
        else:
            vigenere_encrypt_result += char

    return vigenere_encrypt_result


def decrypt_vigenere(auto_decrypted, vigenere_key):
    decrypt_vigenere_result = ""
    vigenere_key = vigenere_key.upper()
    key_index = 0

    for char in auto_decrypted:
        if char.isalpha():
            c = ord(char.upper()) - ord('A')
            k = ord(vigenere_key[key_index % len(vigenere_key)]) - ord('A')
            vigenere_decrypted = chr((c - k) % 26 + ord('A'))
            decrypt_vigenere_result += vigenere_decrypted
            key_index += 1
        else:
            decrypt_vigenere_result += char

    return decrypt_vigenere_result


def encrypt_caesar(caeser_text, caeser_key):
    encrypt_caesar_result = ""

    for char in caeser_text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr(
                (ord(char) - base + caeser_key) % 26 + base
            )
            encrypt_caesar_result += encrypted
        else:
            encrypt_caesar_result += char

    return encrypt_caesar_result


def decrypt_caesar(caeser_text, caeser_key):
    return encrypt_caesar(caeser_text, -caeser_key)


# Main program
caeser_plaintext = input("Enter Ceasar plaintext: ")
caeser_key = int(input("Enter Caesar key: "))

caesar_ciphertext = encrypt_caesar(caeser_plaintext, caeser_key)
print("Caesar Cipher:", caesar_ciphertext)
print(\n)
print("Vigenere PlainText:",caesar_ciphertext)
vigenere_plaintext = caesar_ciphertext
vigenere_key = input("Enter Vigenere keyword: ")

vigenere_ciphertext = encrypt_vigenere(
    vigenere_plaintext, vigenere_key
)
print("Vigenere Cipher:", vigenere_ciphertext)

print(\n)
print("Auto PlainText:",vigenere_ciphertext)
auto_plaintext = vigenere_ciphertext
auto_key = input("Enter initial Autokey keyword: ")

auto_ciphertext, keystream = encrypt_autokey(
    auto_plaintext, auto_key
)
print("Autokey Cipher:", auto_ciphertext)
print("Generated Key Stream:", keystream)

print(\n,\n)
auto_decrypted = decrypt_autokey(auto_ciphertext, auto_key)
print("Autokey Decrypted:", auto_decrypted)

vigenere_decrypted = decrypt_vigenere(
    auto_decrypted, vigenere_key
)
print("Vigenere Decrypted:", vigenere_decrypted)

caesar_decrypted = decrypt_caesar(
    vigenere_decrypted, caeser_key
)
print("Caesar Decrypted:", caesar_decrypted)