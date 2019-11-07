import random
import string
import os

msg = ''.join(random.choice(string.ascii_lowercase) for i in range(1024))
assert decrypt(key, iv, encrypt(key, iv, msg)) == msg

