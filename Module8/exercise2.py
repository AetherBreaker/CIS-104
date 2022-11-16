import os

from Module7.exercise2 import recurse_dir_search

if __name__ == "__main__":
    fpath = recurse_dir_search(
        "mbox-short.txt", os.path.dirname(os.path.abspath(__file__))
    )
    fhand = open(fpath)
    count = 0
    for line in fhand:
        words = line.split()
        # print('Debug:', words)
        if (
            len(words) < 3
        ):  # Now checks for lenths less than three, instead of just length 0
            continue
        if words[0] != "From":
            continue
        print(words[2])
