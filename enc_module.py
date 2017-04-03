""" AES Encryption part was referenced from Eli's blog """

from os import urandom
from hashlib import md5
from Crypto.Cipher import AES

def derive_keyand_iv(password, salt, key_length, iv_length):
  d = d_i = b''
  while len(d) < key_length + iv_length:
    d_i = md5(d_i + str.encode(password) + salt).digest()
    d += d_i
  return d[:key_length, d[key_length:key_length + iv_length]

def encrypt_file(infile, outfile, password, salt_header='', key_length = 32):
  bs = AES.block_size
  
