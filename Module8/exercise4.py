import os
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from Module7.exercise2 import recurse_dir_search

fname = input("Enter file name: ")
path = recurse_dir_search(fname, os.path.dirname(os.path.abspath(__file__)))
wordset = set()

with open(path) as fh:

    for line in fh:
        line = line.rstrip().split()
        for word in line:
            wordset.add(word)
    print(sorted(wordset))
