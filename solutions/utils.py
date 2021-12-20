import binascii


def bytes2int(b: bytes) -> int:
    return int.from_bytes(b, "big")


def int2bytes(i: int) -> bytes:
    return i.to_bytes((i.bit_length() + 7) // 8, "big")


def bin2txt(x: bytes) -> str:
    return x.decode()


def bin2hex(x: bytes) -> str:
    return bin2txt(binascii.hexlify(x))


def txt2bin(x: str) -> bytes:
    return x.encode()


def hex2bin(x: str) -> bytes:
    return binascii.unhexlify(x)


def hex2txt(x: str) -> str:
    return bin2txt(hex2bin(x))


def txt2hex(x: str) -> str:
    return bin2hex(txt2bin(x))
