#!/usr/bin/python3

import base64

encoded_password = "WW91IHJlYWxseSB0aG91Z2h0IEkgd291bGQgbGV0IG15IHBhc3N3b3JkIGhlcmU/ISA6RA=="
decoded_password = base64.b64decode(encoded_password).decode('utf-8')
print(decoded_password)

