import os
import re
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

if __name__ == "__main__":
    fpath = input("Enter a file name: ")

    with open(fpath, "r") as fhand:
        print(fpath, sum(int(x) for x in re.findall(r"[0-9]+", fhand.read())))
