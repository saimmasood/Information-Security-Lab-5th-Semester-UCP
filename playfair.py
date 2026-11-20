def prepare_key(key):
    key = key.upper()

    result = ""
    used = set()

    for char in key:

        if char.isalpha():

            if char == 'J':
                char = 'I'

            if char not in used:
                result += char
                used.add(char)

    return result


def create_matrix(key):
    key = prepare_key(key)

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    matrix_text = ""

    # Add keyword
    for char in key:
        if char not in matrix_text:
            matrix_text += char

    # Add remaining alphabet
    for char in alphabet:
        if char not in matrix_text:
            matrix_text += char

    # Convert into 5x5 matrix
    matrix = []

    for i in range(0, 25, 5):
        matrix.append(list(matrix_text[i:i+5]))

    return matrix


def display_matrix(matrix):
    print("\nPlayfair Matrix:")

    for row in matrix:
        print(" ".join(row))


def find_position(matrix, char):

    if char == 'J':
        char = 'I'

    for row in range(5):
        for col in range(5):

            if matrix[row][col] == char:
                return row, col

    return None


def prepare_plaintext(text):

    text = text.upper()

    # Remove non-alphabetic characters
    clean = ""

    for char in text:
        if char.isalpha():
            if char == 'J':
                char = 'I'

            clean += char

    result = ""

    i = 0

    while i < len(clean):

        first = clean[i]

        if i + 1 < len(clean):

            second = clean[i + 1]

            # Repeated letters
            if first == second:
                result += first + 'X'
                i += 1

            else:
                result += first + second
                i += 2

        else:
            # Odd number of characters
            result += first + 'X'
            i += 1

    return result


def encrypt_pair(matrix, a, b):

    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    # Same row
    if row1 == row2:

        new_a = matrix[row1][(col1 + 1) % 5]
        new_b = matrix[row2][(col2 + 1) % 5]

    # Same column
    elif col1 == col2:

        new_a = matrix[(row1 + 1) % 5][col1]
        new_b = matrix[(row2 + 1) % 5][col2]

    # Rectangle
    else:

        new_a = matrix[row1][col2]
        new_b = matrix[row2][col1]

    return new_a + new_b


def decrypt_pair(matrix, a, b):

    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    # Same row
    if row1 == row2:

        new_a = matrix[row1][(col1 - 1) % 5]
        new_b = matrix[row2][(col2 - 1) % 5]

    # Same column
    elif col1 == col2:

        new_a = matrix[(row1 - 1) % 5][col1]
        new_b = matrix[(row2 - 1) % 5][col2]

    # Rectangle
    else:

        new_a = matrix[row1][col2]
        new_b = matrix[row2][col1]

    return new_a + new_b


def encrypt_playfair(plaintext, matrix):

    prepared = prepare_plaintext(plaintext)

    ciphertext = ""

    for i in range(0, len(prepared), 2):

        pair = encrypt_pair(
            matrix,
            prepared[i],
            prepared[i + 1]
        )

        ciphertext += pair

    return ciphertext, prepared


def decrypt_playfair(ciphertext, matrix):

    plaintext = ""

    for i in range(0, len(ciphertext), 2):

        pair = decrypt_pair(
            matrix,
            ciphertext[i],
            ciphertext[i + 1]
        )

        plaintext += pair

    return plaintext


# Main program

key = input("Enter keyword: ")
plaintext = input("Enter plaintext: ")

matrix = create_matrix(key)

display_matrix(matrix)

ciphertext, prepared = encrypt_playfair(
    plaintext,
    matrix
)

print("\nPrepared Plaintext:", prepared)
print("Ciphertext:", ciphertext)

decrypted = decrypt_playfair(
    ciphertext,
    matrix
)

print("Decrypted Text:", decrypted)