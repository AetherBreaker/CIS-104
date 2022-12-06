import os
import re
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

count = {}


if __name__ == "__main__":
    fpath = recurse_dir_search(input("Enter a file name: "))
    with open(fpath) as fhand:
        contents = fhand.read()

    contents = re.sub(r"[^a-z]", "", contents.casefold())

    for char in contents:
        count[char] = count.get(char, 0) + 1

    total = sum(count.values())
    for char, cnt in count.items():
        count[char] = cnt / total

    count = sorted(count.items(), key=lambda x: x[1], reverse=True)

    print("\n".join(f"{char} {freq}" for char, freq in count))
