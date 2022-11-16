import os
import re
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from Module7.exercise2 import recurse_dir_search

matchpat = re.compile(r"From[^:]")

fname = input("Enter file name: ")
path = recurse_dir_search(fname, os.path.join(os.getcwd(), "Module7"))
count = 0

with open(path) as fh:
    for line in fh:
        if matchpat.match(line):
            count += 1
            print(line.strip().split()[1])

print(f"There were {count} lines in the file with From as the first word")
