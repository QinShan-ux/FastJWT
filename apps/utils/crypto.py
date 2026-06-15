import base64
import json
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

SECRET_KEY = b"1234567890abcdef"  # 16/24/32 字节

def aes_encrypt(data: str) -> str:
    nonce = get_random_bytes(16)
    cipher = AES.new(SECRET_KEY, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(data.encode())
    result = {
        "nonce": base64.b64encode(nonce).decode(),
        "tag": base64.b64encode(tag).decode(),
        "data": base64.b64encode(ciphertext).decode(),
    }
    return base64.b64encode(json.dumps(result).encode()).decode()

def aes_decrypt(data: str) -> str:
    result = json.loads(base64.b64decode(data).decode())
    nonce = base64.b64decode(result["nonce"])
    tag = base64.b64decode(result["tag"])
    ciphertext = base64.b64decode(result["data"])
    cipher = AES.new(SECRET_KEY, AES.MODE_GCM, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode()