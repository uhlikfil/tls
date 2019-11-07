# TLS protocol
THe goal of this lab is to get familiar with underlying principals of SSL/TLS cryptographic protocol.

## Task 1: Diffie–Hellman key exchange
Implement the [vanilla](https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#Cryptographic_explanation) DH algorithm
Try it with ``p=37`` and `g=5`. Can you make it working with a recommended values 
``p=0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF``
and ``g=2`` ?

## Task 2: Diffie–Hellman key 
Turn a DH secret into a key. Use ``sha1`` to generate `BLOCK_SIZE = 16` long key material

## Task 3: Bulk cipher
Ensure you have working implementation of AES in CBC mode with PKCS&#35;7 padding. It is recommended to use  `BLOCK_SIZE = 16`
You will need ``encrypt(key, iv, message)`` and `decrypt(key, iv, encrypted_message)` functions.
You can check you implementation with ``bulk_cipher.py`` example.
