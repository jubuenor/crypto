def ecb_encrypt(plaintext, pi):
    ciphertext = ''
    n = len(pi)
    m = len(plaintext) // n
    
    for i in range(m):
        block = plaintext[i*n:(i+1)*n]
        permuted_block = ''.join([block[pi[j]-1] for j in range(n)])
        ciphertext += permuted_block
    
    return ciphertext

def main():
    m = 4 #int(input("Enter block size (m): "))
    plaintext = "1011000101001010" #input("Enter plaintext: ").strip()
    pi = tuple(([1, 2, 3, 4] , [2, 3, 4, 1]))
    
    ciphertext = ecb_encrypt(plaintext, pi)
    print("Encrypted text:", ciphertext)

if __name__ == "__main__":
    main()
