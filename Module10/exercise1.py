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
    targetpattern = re.compile(r"From[^:]")
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.match(line):
                domain = line.strip().split()[1]
                if domain not in count:
                    count[domain] = 1
                else:
                    count[domain] += 1

    count = sorted(
        ((cnt, email) for email, cnt in count.items()), reverse=True, key=lambda x: x[0]
    )
    print((mx := max(count, key=lambda x: x[0]))[1], mx[0])
