#!/bin/python3

import sys
import zlib
import base64
import json

if __name__ == "__main__":
    jwt = bytearray()

    if sys.stdin.isatty():
        print("That's not how it works...")
        exit(1)

    while (byte := sys.stdin.read(1)):
        if byte == '/':
            break

    while (byte := sys.stdin.read(2)):
        try:
            jwt.append(int(byte) + 45)
        except ValueError:
            pass

    header, payload, signature = jwt.decode().split('.')

    while len(payload) % 4 != 0:
        payload += '='

    z = zlib.decompressobj(-15)
    decompressed = z.decompress(base64.urlsafe_b64decode(payload))

    print(json.dumps(json.loads(decompressed), indent = 2))
