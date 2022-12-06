import os
import re
import sys
from datetime import datetime

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

if __name__ == "__main__":
    count = 0
    file = "mbox.txt"
    fpath = recurse_dir_search(file)
    inp = input("Enter a regular expression: ")
    targetpattern = re.compile(inp)
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.search(line):
                count += 1
    print(f"{file} had {count} lines that matched {inp}")
