import zlib

import brotli

with open("ascii-art.ans", "rb") as text:
    content = brotli.decompress(text.read()).decode()
    with open("ascii-art.ans", "wb") as text:
        text.write(zlib.compress(content.encode()))
