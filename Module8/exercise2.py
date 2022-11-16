import os

from Module7.exercise2 import recurse_dir_search

if __name__ == "__main__":
    fpath = recurse_dir_search(
        "Exercise 2.py", os.path.dirname(os.path.abspath(__file__))
    )
    fhand = open("mbox-short.txt")
    count = 0
    for line in fhand:
        words = line.split()
        # print('Debug:', words)
        if len(words) == 0:
            continue
        print(words[2])
