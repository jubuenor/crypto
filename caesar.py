A = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def encrypt(plain_text, k):
    cipher_text = ""
    plain_text= plain_text.split(" ")
    for word in plain_text:
        for letter in word:
            cipher_text += A[(A.index(letter) + k) % 26]
        cipher_text += " "
    
    return cipher_text

def decrypt(cipher_text, k):
    plain_text = ""
    cipher_text= cipher_text.split(" ")
    for word in cipher_text:
        for letter in word:
            plain_text += A[(A.index(letter) - k) % 26]
        plain_text += " "
    return plain_text

def split_text(text, m):
    text = text.upper().replace(" ", "")
    text = [text[i:i+m] for i in range(0, len(text), m)]
    return ' '.join(text)

plain_text = "hmwnxytumjw" #input("Enter the plain text: ")
k = 5 # int(input("Enter the value of k: "))
m = 5 # int(input("Enter the value of m: "))
mode = "decrypt" # input("Enter the mode (encrypt/decrypt): ")


plain_text = split_text(plain_text, m)

if mode == "encrypt":
    print(encrypt(plain_text, k))
elif mode == "decrypt":
    print(decrypt(plain_text, k))
else:
    print("Invalid mode")

