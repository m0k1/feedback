
from Crypto.Hash import MD5 as md5 # digest_size = 16
from Crypto.Hash import RIPEMD as ripemd # digest_size = 20
from Crypto.Hash import SHA as sha1 # digest_size = 20
from Crypto.Hash import SHA224 as sta224 # digest_size = 28
from Crypto.Hash import SHA256 as sha256 # digest_size = 32
from Crypto.Hash import SHA384 as sha384 # digest_size = 48
from Crypto.Hash import SHA512 as sha512 # digest_size = 64
from libonetimepadcypher import cypher

def md5_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = md5.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = md5.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = md5.new(pad)
        h3 = hash_3.digest()
        key += h3
        pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def ripemd_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = ripemd.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = ripemd.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = ripemd.new(pad)
        h3 = hash_3.digest()
        key += h3
    pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def sha1_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = sha1.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = sha1.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = sha1.new(pad)
        h3 = hash_3.digest()
        key += h3
    pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def sha256_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = sha256.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = sha256.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = sha256.new(pad)
        h3 = hash_3.digest()
        key += h3
    pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def sha224_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = sha224.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = sha224.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = sha224.new(pad)
        h3 = hash_3.digest()
        key += h3
    pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def sha384_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = sha384.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = sha384.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = sha384.new(pad)
        h3 = hash_3.digest()
        key += h3
    pad = cypher(pad,h3)
    del hash_3
    del h3
    return key

def sha512_loop(secret,masterlen):
    key = ''
    pad = ''
    hash_1 = sha512.new(secret)
    h1 = hash_1.digest()
    del secret
    hash_2 = sha512.new(h1)
    h2 = hash_2.digest()
    del hash_1
    del hash_2
    pad = cypher(h1,h2)
    del h1
    del h2
    while len(key) <= masterlen:
        hash_3 = sha512.new(pad)
        h3 = hash_3.digest()
        key += h3
        pad = cypher(pad,h3)
    del hash_3
    del h3
    return key
