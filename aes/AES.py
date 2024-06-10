import base64
import pyaes

file = input("Enter the file name: ")
img = open(file, "rb")
file_data = img.read()


level = int(input("Enter the level of encryption (128, 192, 256): "))

if level == 128:
    key= b'dMj\xc9\xba\x8d\xb5\xc4<\x8c\xeb\x94x\x8c\x86\x86'
elif level == 192:
    key = b'\xc4\xd0\x19\xf8\xa5\x1d0\x9e\x0em\xado\xab7\xfc\xc8)\x0b~\xb4=;\xc4='
elif level == 256:
    key = b'\x00r6\x9d\xa3j3\xb7\xe7$\xf7\x0e\xd6\n\x8d\x1e\xde\xa2\x9e~\xa8\r\xef \xdfYb\xd0\xfc\x83\xffp'
else:
    print("Invalid level of encryption")
    exit(0)

aes = pyaes.AESModeOfOperationCTR(key)
ciphertext = aes.encrypt(file_data)

img_base64 = base64.b64encode(ciphertext)

print("Encrypted data: \n", img_base64)

img_base64 = base64.b64decode(img_base64)

aes = pyaes.AESModeOfOperationCTR(key)

decrypted = aes.decrypt(img_base64)

img_decoded = open("decrypted_" + file, "wb")
img_decoded.write(decrypted)
