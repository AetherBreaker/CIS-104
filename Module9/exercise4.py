import os
import re
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

count = {}


if __name__ == "__main__":
    fpath = recurse_dir_search("mbox-short.txt")
    targetpattern = re.compile(r"From[^:]")
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.match(line):
                user = line.strip().split()[1]
                if user not in count:
                    count[user] = 1
                else:
                    count[user] += 1
    print("{}: {}".format(*max(count.items(), key=lambda x: x[1])))
