##############################
########### Task 8 ###########
##############################

import hashlib

from solutions.rsa import decrypt, encrypt
from solutions.rsa_broadcast_attack import invpow
from solutions.utils import bytes2int, int2bytes

# recommended values
p = 19480788016963928122154998009409704650199579180935803274714730386316184054417141690600073553930946636444075859515663914031205286780328040150640437671830139
q = 17796969605776551869310475203125552045634696428993510870214166498382761292983903655073238902946874986503030958347986885039275191424502139015148025375449097

asn_1 = b"\x30\x21\x30\x09\x06\x05\x2b\x0e\x03\x02\x1a\x05\x00\x04\x14"


def generate_message_hash(msg: bytes):
    return hashlib.sha1(msg).digest()


def generate_signature(private_key: tuple[int], hash: bytes):
    sig = make_padding(private_key[0], len(hash)) + hash
    return decrypt(private_key, sig)


def verify_signature(public_key: tuple[int], signature: bytes, hash: bytes) -> bool:
    decrypted_sig = encrypt(public_key, signature)
    return b"\x00" + asn_1 + hash in decrypted_sig  # very weak verification


def make_padding(n: int, hash_len: int) -> bytes:
    n_byte_len = n.bit_length() // 8
    if n.bit_length() % 8 > 0:
        n_byte_len += 1
    padding_size = n_byte_len - 3 - len(asn_1) - hash_len
    return b"\x00\x01" + b"\xff" * padding_size + b"\x00" + asn_1


def fake_signature(hash: bytes) -> bytes:
    # most significant bits will be the important part
    msb = b"\x00\x01" + b"\xff\x00" + asn_1 + hash
    garbage = b"\xff" * 80
    forged_sig = msb + garbage
    # return the lower bound integer cube root - will mess up the garbage bits, but we don't care
    return int2bytes(invpow(bytes2int(forged_sig), 3))
