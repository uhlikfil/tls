##############################
########## Task 1,2 ##########
##############################

import binascii
import hashlib

# recommended values
P = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF
G = 2


def diffie_hellman(p, g, private_key) -> int:
    return pow(g, private_key, p)


def key_from_secret(secret: int) -> bytes:
    hex_str = hex(secret)[2:]
    # leading zero is sometimes missing making the string odd length
    if len(hex_str) % 2 != 0:
        hex_str = f"0{hex_str}"
    bytes_ = binascii.unhexlify(hex_str[2:])
    return hashlib.sha1(bytes_).digest()[:16]


if __name__ == "__main__":
    A_PRIV = 125
    B_PRIV = 111
    g2a = diffie_hellman(P, G, A_PRIV)  # is sent to B
    g2b = diffie_hellman(P, G, B_PRIV)  # is sent to A

    a_final = diffie_hellman(P, g2b, A_PRIV)
    b_final = diffie_hellman(P, g2a, B_PRIV)

    assert a_final == b_final

    key = key_from_secret(a_final)
