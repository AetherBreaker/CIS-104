import os
import re

# recursion = 0
# TABCHAR = "\t"


def recurse_dir_search(filetarget: str, current_directory: str):
    """This is just a custom function for recursively searching the entire current directory
    for the inputed file, including searching through all subfolders.

    The commented print functions are from debugging, they use the commented global var recursion
    combined with tab characters to track how many layers deep into recursion the function goes
    during execution.
    """
    # global recursion
    # recursion += 1
    path = current_directory
    # print(f"{recursion*TABCHAR}{path}")
    dirlist = os.listdir(path)
    # print(f"{recursion*TABCHAR}for loop:")
    for filename in dirlist:
        # print(f"{recursion*TABCHAR}\t{filename}")
        if filename == filetarget:
            path = os.path.join(current_directory, filetarget)
            # print(f"{recursion*TABCHAR}\t{path}")
            return path
        elif not validext.search(filename):
            try:
                return recurse_dir_search(filetarget, os.path.join(path, filename))
            except FileNotFoundError:
                continue
    # print(f"{recursion*TABCHAR}end loop")
    # recursion -= 1
    raise (FileNotFoundError)


"""This detects whether this python module is being ran as a script, or being imported
if it is being ran directly, the builtin __name__ variable will equal "__main__" otherwise
if the module has been imported, __name__ will equal the name of the module.

This allows you to run this file as a script, while still allowing you to import the recurse_dir_search
func for use in other python modules without accidentally running the script below.
"""
if __name__ == "__main__":
    MODDIR = os.path.abspath(__file__)
    curdir = os.path.dirname(MODDIR)

    uinput = input("Enter a file name:")

    validext = re.compile(r"\.[a-zA-Z]{2,4}$")

    if not validext.search(uinput):
        print(f"{uinput} doesn't have a valid file extension")
        quit()

    target = recurse_dir_search(uinput, curdir)
    total, count = 0, 0.0
    with open(target, "r") as file:
        for line in file:
            if not line.startswith("X-DSPAM-Confidence:"):
                continue
            line = line.strip().partition(" ")
            total += float(line[2])
            count += 1
    print(f"Average spam confidence: {total/count}")
