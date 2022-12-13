import os
import re
import sys

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

if __name__ == "__main__":
    file = input("Enter a file name: ")

    validext = re.compile(r"\.[a-zA-Z]{2,4}$")
    if not validext.search(file):
        print(f"{file} doesn't have a valid file extension")
        quit()

    fpath = recurse_dir_search(file)

    with open(fpath, "r") as fhand:
        print(
            file,
            sum(
                occurences := [
                    int(x)
                    for x in re.findall(r"(?<=New Revision: )[0-9]+", fhand.read())
                ]
            )
            // len(occurences),
        )
