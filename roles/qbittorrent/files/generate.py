#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import sys
import codecs
import binascii
from backports.pbkdf2 import pbkdf2_hmac

salt = sys.argv[1].encode("utf8")
password = sys.argv[2].encode("utf8")
key = pbkdf2_hmac("sha512", password, salt, 100000, 64)
b64 = codecs.encode(codecs.decode(binascii.hexlify(key), 'hex'), 'base64').decode()

print(b64.strip())