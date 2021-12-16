##############################
########### Task 3 ###########
##############################

from solutions.aes_cbc import BLOCK_SIZE, decrypt_aes_cbc, encrypt_aes_cbc
from solutions.utils import bin2txt, txt2bin


def encrypt(key: bytes, iv: bytes, message: str) -> bytes:
    return encrypt_aes_cbc(txt2bin(message), key, iv)


def decrypt(key: bytes, iv: bytes, encrypted_message: bytes) -> str:
    return bin2txt(decrypt_aes_cbc(encrypted_message, key, iv))
