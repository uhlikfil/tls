##############################
########### Task 4 ###########
##############################

import os
import sys

from solutions.aes_interface import BLOCK_SIZE, decrypt, encrypt
from solutions.diffie_hellman import G, P, diffie_hellman, key_from_secret


class Agent:
    def __init__(self, msg=None, p=P, g=G) -> None:
        self.msg = msg
        self.p = p
        self.g = g
        self.private_key = int.from_bytes(os.urandom(4), sys.byteorder)
        self.shared_key = None

    def receive_public_data(self, p, g):
        self.p = p
        self.g = g

    def send_public_data(self):
        return self.p, self.g

    def receive_public_key(self, key):
        shared_secret = diffie_hellman(self.p, key, self.private_key)
        self.shared_key = key_from_secret(shared_secret)

    def send_public_key(self):
        return diffie_hellman(self.p, self.g, self.private_key)

    def receive_message(self, msg: bytes):
        iv = msg[:BLOCK_SIZE]
        encrypted_msg = msg[BLOCK_SIZE:]
        self.msg = decrypt(self.shared_key, iv, encrypted_msg)

    def send_message(self):
        iv = os.urandom(BLOCK_SIZE)
        return iv + encrypt(self.shared_key, iv, self.msg)
