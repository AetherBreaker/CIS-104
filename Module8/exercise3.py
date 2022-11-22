import os
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

if __name__ == "__main__":
    fpath = recurse_dir_search("mbox-short.txt")
    with open(fpath) as fhand:
        count = 0
        for line in fhand:
            words = line.split()
            # print('Debug:', words)
            if len(words) < 3 or words[0] != "From":
                continue
            print(words[2])
