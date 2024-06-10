import numpy as np

def turning_grill_encrypt(size, direction, grill, message):
    newGrill = np.zeros((size, size), dtype=str)
    n = 0

    while n < len(message):
        for j in range(size):
            for k in range(size):
                if grill[j][k] == True:
                    newGrill[j][k] = message[n] 
                    n += 1
        grill = np.rot90(grill, direction)

    result = ''

    for i in range(size):
        for j in range(size):
            result += newGrill[i][j]
        result += ' '

    return result


def turning_grill_decrypt(size, direction, grill, message):
    newGrill = np.zeros((size, size), dtype=str)
    for i in range(size):
        for j in range(size):
            newGrill[i][j] = message[i*size + j]
    result = ''
    n = 0
    while n < len(message):
        for j in range(size):
            for k in range(size):
                if grill[j][k] == True:
                    result += newGrill[j][k]
                    n += 1
        grill = np.rot90(grill, direction)
        result += ' '
    return result

def getGrill(size):
    grill = np.zeros((size, size), dtype=bool)
    for i in range(size):
        inp = input(f'Enter holes for row {i}: ')
        for j in inp.split():
            grill[i][int(j)] = True
    return grill

def rotateGrill(grill, direction):
    return np.rot90(grill, direction)

size = int(input("Enter size of grill: "))
clockwise = input('1. Clockwise\n2. Counter-clockwise\nChoose direction:') 
direction = 1 if clockwise else -1
grill = getGrill(size)
message = input('Enter message: ').upper().replace(' ', '')
mode = int(input('1. Encrypt\n2. Decrypt\nChoose mode: '))

if mode == 1:
    result = turning_grill_encrypt(size, direction, grill, message)
    print(result)
else:
    result = turning_grill_decrypt(size, direction, grill, message)
    print(result)

