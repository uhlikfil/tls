##############################
########### Task 6 ###########
##############################

import math

from solutions.utils import bytes2int, int2bytes

# recommended values
P = 13604067676942311473880378997445560402287533018336255431768131877166265134668090936142489291434933287603794968158158703560092550835351613469384724860663783
Q = 20711176938531842977036011179660439609300527493811127966259264079533873844612186164429520631818559067891139294434808806132282696875534951083307822997248459


def generate_key(p=P, q=Q, e=3):
    n = p * q
    carm_n = math.lcm(p - 1, q - 1)
    assert math.gcd(carm_n, e) == 1
    d = pow(e, -1, carm_n)
    return (n, d), (n, e)


def encrypt(public_key, msg: bytes) -> bytes:
    # no padding, sadface
    c = encrypt_int(public_key, bytes2int(msg))
    return int2bytes(c)


def decrypt(private_key, encrypted_msg: bytes) -> bytes:
    return encrypt(private_key, encrypted_msg)


def encrypt_int(public_key, num: int) -> int:
    return pow(num, public_key[1], public_key[0])


def decrypt_int(private_key, num: int) -> int:
    return encrypt_int(private_key, num)
