##############################
########### Task 8 ###########
##############################

import hashlib

from solutions.rsa import bytes2int, decrypt, encrypt, int2bytes

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
    return hash in decrypted_sig  # very weak verification


def make_padding(n: int, hash_len: int) -> bytes:
    n_byte_len = n.bit_length() // 8
    if n.bit_length() % 8 > 0:
        n_byte_len += 1
    padding_size = n_byte_len - 3 - len(asn_1) - hash_len
    return b"\x00\x01" + b"\xff" * padding_size + b"\x00" + asn_1


def fake_signature(hash: bytes) -> bytes:
    # make N divisible by 3
    tmp = b"\x00" + asn_1 + hash
    n = 2 ** 288 - bytes2int(tmp)
    tmp += int2bytes(n % 3)
    N = 2 ** 288 - bytes2int(tmp)
    # do magic - now `forged_sig ** 3` contains `tmp`
    forged_sig = 2 ** 1000 - N // 3
    return int2bytes(forged_sig)
