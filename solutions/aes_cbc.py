##############################
########### Task 3 ###########
### taken from crypto labs ###
##############################

import math
import sys

import pyaes

BLOCK_SIZE = 16


def repeat_key(key: bytes, wanted_len: int) -> bytes:
    repeats = math.ceil(wanted_len / len(key))
    return (key * repeats)[:wanted_len]


def xor(text: bytes, key: bytes, byteorder=sys.byteorder) -> bytes:
    if len(key) > len(text):  # always have text as the longer string
        text, key = key, text
    length = len(text)
    key = repeat_key(key, length)
    int_text = int.from_bytes(text, byteorder)
    int_key = int.from_bytes(key, byteorder)
    return (int_text ^ int_key).to_bytes(length, byteorder)


def encrypt_aes_block(text: bytes, key: bytes) -> bytes:
    if len(text) != BLOCK_SIZE or len(key) != BLOCK_SIZE:
        raise ValueError(f"Can only encrypt blocks of size {BLOCK_SIZE} B")
    return pyaes.AESModeOfOperationECB(key).encrypt(text)


def decrypt_aes_block(ct: bytes, key: bytes) -> bytes:
    if len(ct) != BLOCK_SIZE or len(key) != BLOCK_SIZE:
        raise ValueError(f"Can only decrypt blocks of size {BLOCK_SIZE} B")
    return pyaes.AESModeOfOperationECB(key).decrypt(ct)


def pad(text: bytes) -> bytes:
    pad_size: int = BLOCK_SIZE - (len(text) % BLOCK_SIZE)
    to_append = pad_size.to_bytes(1, "big") * pad_size
    return text + to_append


def unpad(text: bytes) -> bytes:
    pad_size: int = text[-1]
    return text[:-pad_size]


def get_blocks(text: bytes) -> list[bytes]:
    return [
        text[i * BLOCK_SIZE : (i + 1) * BLOCK_SIZE]
        for i in range(len(text) // BLOCK_SIZE)
    ]


def encrypt_aes_cbc(text: bytes, key: bytes, iv: bytes) -> bytes:
    if len(key) != BLOCK_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError(f"Can only encrypt with a key and IV of size {BLOCK_SIZE} B")
    padded = pad(text)
    ct = b""
    last_block = iv
    for pt_block in get_blocks(padded):
        to_encrypt = xor(pt_block, last_block)
        last_block = encrypt_aes_block(to_encrypt, key)
        ct += last_block
    return ct


def decrypt_aes_cbc(text: bytes, key: bytes, iv: bytes, keep_padding=False) -> bytes:
    if len(text) % BLOCK_SIZE != 0 or len(key) != BLOCK_SIZE or len(iv) != BLOCK_SIZE:
        raise ValueError(f"Can only decrypt text of length of multiples of {BLOCK_SIZE} with a key and IV of size {BLOCK_SIZE} B")  # fmt: skip
    pt = b""
    last_block = iv
    for ct_block in get_blocks(text):
        decrypted = decrypt_aes_block(ct_block, key)
        pt += xor(decrypted, last_block)
        last_block = ct_block
    return pt if keep_padding else unpad(pt)
