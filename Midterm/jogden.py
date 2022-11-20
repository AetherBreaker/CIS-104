import os
import re


def recurse_dir_search(filetarget: str, current_directory: str):
    validext = re.compile(r"\.[a-zA-Z]{2,4}$")
    path = current_directory
    dirlist = os.listdir(path)
    for filename in dirlist:
        if filename == filetarget:
            path = os.path.join(current_directory, filetarget)
            return path
        elif not validext.search(filename):
            try:
                return recurse_dir_search(filetarget, os.path.join(path, filename))
            except FileNotFoundError:
                continue
    raise (FileNotFoundError)


if __name__ == "__main__":
    MODDIR = os.path.abspath(__file__)
    curdir = os.path.dirname(MODDIR)

    target = recurse_dir_search("cheeses.txt", curdir)

    cheeses = []  # if there was a chance of duplicates, this should be a set() instead
    # sets can only be added to and are otherwise immutable, and can only contain
    # one of each value. Equality is determined by comparing the hash of each value.

    with open(target, "r") as file:
        for line in file:
            listcomprehensionjank = [cheeses.append(cheese) for cheese in line.split()]
            # this is a list comprehension, it's a way to create a list from a for loop in one line
            # however since list.append() returns None, this will just result in a list of Nones
            # but it still appends the values to the cheeses list.
            # normally you really shouldnt use list comprehensions for something like this
            # just use a normal for loop. I really just did it because I felt like it :).

    cheeses.sort()
    # sort the list in place.
    # If you were using a set, you would have to do "cheeses = sorted(cheeses)" instead as
    # sets are immutable.
    # sorted() returns a new list with the values sorted, so it would need to be performed in a
    # variable assignment.

    prettyprinted = "\n    ".join(cheeses)
    # fstrings dont like \ escape characters inside curly brackets so I have to prepare
    # this ahead of time.
    print(f"cheeses = [\n    {prettyprinted}\n]")
