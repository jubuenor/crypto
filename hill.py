import numpy as np
from textwrap import wrap

ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain, key, t):
    if np.linalg.det(key) == 0:
        raise ValueError('Invalid key')

    result = ''

    for char in wrap(plain, t):
        c = np.array([ABC.index(x) for x in char]) 
        mul = np.dot(c, key) % 26

        for i in range(t):
            result += ABC[mul[i]]

    return result

def decrypt(cipher, key, t):
    if np.linalg.det(key) == 0:
        raise ValueError('Invalid key')

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

message = 'JULY'
key = np.array([[11, 8], [3, 7]])

encrypted = encrypt(message, key, 2)
print(encrypted)
decrypted = decrypt(encrypted, key, 2)
print(decrypted)

