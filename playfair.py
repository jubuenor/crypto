# Playfair cipher implementation

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

def clean_key(key):
    return key.upper().replace('J', 'I').replace(' ', '')

def clean_text(plaintext):
    plaintext = plaintext.upper().replace('J', 'I').replace(' ', '')
    if len(plaintext) % 2 == 1:
        plaintext += 'X'
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    return digraphs

def generate_matrix(key):
    matrix = []
    key_square = ''
    for char in key + alphabet:
        if char not in key_square:
            key_square += char

    return key_square

def encrypt(diagraph,matrix):
    a, b = diagraph
    row_a, col_a = divmod(matrix.index(a), 5)
    row_b, col_b = divmod(matrix.index(b), 5)
    if row_a == row_b:
        col_a, col_b = (col_a + 1) % 5, (col_b + 1) % 5
    elif col_a == col_b:
        row_a, row_b = (row_a + 1) % 5, (row_b + 1) % 5
    else:
        col_a, col_b = col_b, col_a

    return matrix[row_a * 5 + col_a] + matrix[row_b * 5 + col_b]

def decrypt(diagraph, matrix):
    a, b = diagraph
    row_a, col_a = divmod(matrix.index(a), 5)
    row_b, col_b = divmod(matrix.index(b), 5)

    if row_a == row_b:
        col_a, col_b = (col_a - 1) % 5, (col_b - 1) % 5
    elif col_a == col_b:
        row_a, row_b = (row_a - 1) % 5, (row_b - 1) % 5
    else:
        col_a, col_b = col_b, col_a

    return matrix[row_a * 5 + col_a] + matrix[row_b * 5 + col_b]

def playfair_encrypt(plaintext, key, mode):
    plaintext = clean_text(plaintext)
    key = clean_key(key)
    matrix = generate_matrix(key)
    result = ''
    for diagraph in plaintext:
        if mode == 'encrypt':
            result += encrypt(diagraph, matrix)
        else:
            result += decrypt(diagraph, matrix)

    return result

plaintext = input('Enter plaintext: ') # 'HELLO WORLD' 
key = input('Enter key: ') # 'MONARCHY'
mode = input('Enter mode: ') # 'encrypt' or 'decrypt'

if mode == 'encrypt':
    print('Encrypted:', playfair_encrypt(plaintext, key, mode))
else:
    print('Decrypted:', playfair_encrypt(plaintext, key, mode))

