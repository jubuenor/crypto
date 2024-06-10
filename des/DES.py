import base64
import pyDes    

file = input("Enter the file name: ")
image = open(file, "rb")

file_data = image.read()
byte_array = bytearray(file_data)

key = input("Enter the key: ")

des = pyDes.des(key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
cipher_text = des.encrypt(byte_array)

img_base64_encode = base64.b64encode(cipher_text)
print(img_base64_encode)

img_base64_decode = base64.b64decode(img_base64_encode)

decipher_text = des.decrypt(img_base64_decode)
img_result = open("result.jpg", "wb")
img_result.write(decipher_text)
