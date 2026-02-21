from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
import time
from utils import pad

with open("sample.txt", "rb") as f:
    message = f.read()

print("Original Message:", message)
print("-"*40)

# AES
key_aes = get_random_bytes(16)
aes_msg = pad(message, 16)

start=time.time()
cipher=AES.new(key_aes, AES.MODE_ECB)
enc=cipher.encrypt(aes_msg)
aes_enc=time.time()-start

start=time.time()
dec=cipher.decrypt(enc)
aes_dec=time.time()-start

print("AES encrypted:", enc)
print("AES decrypted:", dec)
print("AES time:", aes_enc)

print("-"*40)

# DES
key_des = get_random_bytes(8)
des_msg = pad(message, 8)

start=time.time()
cipher=DES.new(key_des, DES.MODE_ECB)
enc=cipher.encrypt(des_msg)
des_enc=time.time()-start

start=time.time()
dec=cipher.decrypt(enc)
des_dec=time.time()-start

print("DES encrypted:", enc)
print("DES decrypted:", dec)
print("DES time:", des_enc)