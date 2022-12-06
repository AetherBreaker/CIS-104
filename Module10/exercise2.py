import os
import re
import sys
from datetime import datetime

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

count = []


if __name__ == "__main__":
    fpath = recurse_dir_search(input("Enter a file name: "))
    targetpattern = re.compile(r"From[^:]")
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.match(line):
                line = line.strip().split()
                user = line[1]
                time = datetime.strptime(" ".join(line[2:]), "%a %b %d %H:%M:%S %Y")
                print("%H" % time.hour)
                pass
