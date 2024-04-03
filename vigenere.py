import sys

abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

table = []
for i in range(26):
    table.append(abc[i:] + abc[:i])

def encrypt_vigenere(plaintext, keyword):
    result = ''

    for i in range(len(plaintext)):
        if plaintext[i] in abc:
            result += table[abc.index(keyword[i % len(keyword)])][abc.index(plaintext[i])]
        else:
            result += plaintext[i]

    return result

def decrypt_vigenere(plaintext, keyword):
    result = ''

    for i in range(len(plaintext)):
        if plaintext[i] in abc:
            result += abc[table[abc.index(keyword[i % len(keyword)])].index(plaintext[i])]
        else:
            result += plaintext[i]

    return result

def format_plaintext(s,t):
    s = s.upper()
    s = s.replace(' ', '')

    result = ''
    for i in range(len(s)):
        if i % t == 0 and i != 0:
            result += ' ' + s[i]
        else:
            result += s[i]
    return result

def format_keyword(s,n,t):
    s = s.upper()

    result = ''
    for i in range(n):
        if i % t == 0 and i != 0:
            result += ' ' + s[i % len(s)]
        else :
            result += s[i % len(s)]

    return result


#plaintext = 'TO BE OR NOT TO BE THAT IS THE QUESTION'
#keyword = 'RElATIONS'
#t = 5

keyword = sys.argv[1]
t = int(sys.argv[2])
plaintext = sys.argv[3]
mode = sys.argv[4]

if mode == 'encrypt':
    print(encrypt_vigenere(format_plaintext(plaintext,t), format_keyword(keyword,len(format_plaintext(plaintext,t)),t)))
else:
    print(decrypt_vigenere(format_plaintext(plaintext,t), format_keyword(keyword,len(format_plaintext(plaintext,t)),t)))

