import numpy as np
from textwrap import wrap

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain, key, t):
    result = ''

    for char in wrap(plain, t):
        c = np.array([ABC.index(x) for x in char]) 
        mul = np.dot(c, key) % 26

        for i in range(t):
            result += ABC[mul[i]]

    return result

def decrypt(cipher, key, t):
    result = ''

    for char in wrap(cipher, t):
        c = np.array([ABC.index(x) for x in char]) 
        inv = modular_inverse_matrix(key, 26)
        
        mul = np.dot(c, inv) % 26

        for i in range(t):
            result += ABC[mul[i]]

    return result

def modular_inverse_matrix(matrix, modulus):
    det = np.linalg.det(matrix)
    det_inv = pow(int(det), -1, modulus)
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int)
    return (det_inv * adjugate) % modulus

def check_key(key):
    if np.linalg.det(key) == 0:
        raise ValueError('Invalid key')

    if np.linalg.det(key) % 26 == 0:
        raise ValueError('Invalid key')

    if np.gcd(int(np.linalg.det(key)), 26) != 1:
        raise ValueError('Invalid key')

    return True

message = input('Enter message: ').upper()
entries = list(map(int, input('Enter key (2x2): ').split()))
key = np.array(entries).reshape(2, 2)
check_key(key)
mode = int(input('1. Encrypt\n2. Decrypt\nChoose mode: '))

if mode == 1:
    encrypted = encrypt(message, key, 2)
    print(encrypted)
elif mode == 2:
    decrypted = decrypt(message, key, 2)
    print(decrypted)
