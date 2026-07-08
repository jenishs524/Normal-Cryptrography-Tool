from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from hashlib import sha256
import base64

key = sha256(b"mypassword").digest()
pad = lambda d: d + bytes([16 - len(d) % 16]) * (16 - len(d) % 16)
unpad = lambda d: d[:-d[-1]]

def encrypt(m):
    iv = get_random_bytes(16)
    return base64.b64encode(iv + AES.new(key, AES.MODE_CBC, iv).encrypt(pad(m.encode()))).decode()

def decrypt(e):
    d = base64.b64decode(e)
    return unpad(AES.new(key, AES.MODE_CBC, d[:16]).decrypt(d[16:])).decode()

while True:
    c = input("\n1.Encrypt 2.Decrypt 3.Exit: ")
    if c == "1": print(encrypt(input("Msg: ")))
    elif c == "2": print(decrypt(input("Enc: ")))
    else: print("Invalid")

    