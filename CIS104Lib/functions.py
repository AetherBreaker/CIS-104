import os
import re

DATALOC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")


def recurse_dir_search(filetarget: str, current_directory: str = DATALOC) -> str:
    """This is just a custom function for recursively searching the entire current directory
    for the inputed file, including searching through all subfolders.
    """
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
