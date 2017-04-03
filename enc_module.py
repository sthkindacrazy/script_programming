""" AES Encryption part was referenced from Eli's blog """

from os import urandom
from hashlib import md5
from Crypto.Cipher import AES

def derive_keyand_iv(password, salt, key_length, iv_length):
  d = d_i = b''
  while len(d) < key_length + iv_length:
    d_i = md5(d_i + str.encode(password) + salt).digest()
    d += d_i
  return d[:key_length], d[key_length:key_length + iv_length]

def encrypt_file(infile, outfile, password, salt_header='', key_length = 32):
  bs = AES.block_size
  salt = urandom(bs - len(salt_header))
  key, iv = derive_key_and_iv(password, salt, key_length, bs)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  with open(outfile, "wb") as out_file:
    with open(infile, "rb") as in _file:
      out_file.write(str.encode(salt_header) + salt)
      finished = False
      while not finished:
        chunk = in_file.read(1024.bs)
        if (len(chunk) == 0) or ((len(chunk) % bs) != 0):
          padding_length = (bs - len(chunk) % bs) or bs
          chunk += str.encode(padding_length * chr(padding_length))
          finished = True
        out_file.write(cipher.encrypt(chunk))


def decrypt_file(infile, outfile, password, salt_header='', key_length = 32):
  bs = AES.block_size
  with open(infile, "rb") as in_file:
    with open(outfile, "wb") as out_file:
      salt = in_file.read(bs)[len(salt_header):]
      key, iv = derive_key_and_iv(password, salt, key_length, bs)
      cipher = AES.new(key, AES.MODE_CBC, iv)
      next_chunk = b''
      finished = False
      while not finished:
        chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024*bs))
        if not next_chunk:
          padlen = chunk[-1]
          if isinstance(padlen, str):
            padlen = ord(padlen)
            padding = padlen * chr(padlen)
          else:
            padding = (padlen * chr(chunk[-1])).encode()
          
          if padlen < 1 or padlen > bs:
            raise ValueError("bad decrypt pad(%d)" % padlen)
          if chunk[-padlen:] != padding:
            raise ValueError("bad decrypt")
          chunk = chunk[:-padlen]
          finished = True
        out_file.write(chunk)
  
