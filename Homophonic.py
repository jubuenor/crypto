import random

layout={
        "A": [9,12,33,47,53,67,78,92],
        "B": [48,81],
        "C": [13,41,62],
        "D": [1, 3, 45, 79],
        "E": [14,16,24,44,46,55,57,64,74,82,87,98],
        "F": [10, 31],
        "G": [6,25],
        "H": [23,39,50,56,65,68],
        "I": [32,70,73,83,88,93],
        "J": [15],
        "K": [4],
        "L": [26,37,51,84],
        "M": [22, 27],
        "N": [18,58,59,66,71,91],
        "O": [0,5,7,54,72,90,99],
        "P": [38, 95],
        "Q": [94],
        "R": [29,35,40,42,77,80],
        "S": [11,19,36,76,86,96],
        "T": [17,20,30,43,49,69,75,85,97],
        "U": [8,61,63],
        "V": [34],
        "W": [60,89],
        "X": [28],
        "Y": [21,52],
        "Z": [2]
        }

def homophonic_encryption(message):
    message = message.replace(" ", "")

    encrypted_message = ""
    for letter in message:
        encrypted_message += str(layout[letter][random.randint(0,len(layout[letter])-1)]) + " "
    return encrypted_message

def homophonic_decryption(message):
    decrypted_message = ""
    for number in message.split():
        for letter in layout:
            if int(number) in layout[letter]:
                decrypted_message += letter
    return decrypted_message

message = input("Enter a message: ")
mode = input(" 1. Encrypt \n 2. Decrypt \n")
message = message.upper()

if mode == "1":
    print(homophonic_encryption(message))
else:
        print(homophonic_decryption(message))


