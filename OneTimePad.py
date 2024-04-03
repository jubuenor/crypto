abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt(plain, key):
    plain = plain.upper()
    cipher = ''
    for i in range(len(plain)):
        cipher += abc[(abc.index(plain[i]) + abc.index(key[i])) % 26]
    return cipher

def decrypt(cipher, key):
    plain = ''
    for i in range(len(cipher)):
        plain += abc[(abc.index(cipher[i]) - abc.index(key[i])) % 26]
    return plain

plaintext = 'HELLO'
key = 'EOXJF'

ciphertext = encrypt(plaintext, key)
print("Ciphertext: " + ciphertext)
print("Plaintext: " + decrypt(ciphertext, key))

