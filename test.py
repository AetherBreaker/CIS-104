import os
import sys
import zlib

import brotli

with open("ascii-art.ans", "rb") as text:
    for line in brotli.decompress(text.read()).decode().splitlines():
        print(line)
