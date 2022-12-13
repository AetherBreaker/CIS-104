<<<<<<< HEAD
# Install the required modules `validators` and `yarl` by running
# `pip install validators` and `pip install yarl` in your terminal
import socket

import validators
from yarl import URL

# Prompt the user to enter a URL
# Use URL class from yarl to parse the inputted URL
# Use validators module to check if the URL is valid
# If the URL is not valid, print an error message and prompt the user again
while not (result := validators.url(str(inputted_url := URL(input("Enter a URL: "))))):
    print(f"{inputted_url.human_repr()} is not a valid URL.")
    inputted_url = URL(input("Enter a URL: "))

# Once a valid URL is entered, use socket module to connect to the URL's host on port 80
# Send a GET request to the URL using HTTP/1.0 protocol
# Continuously receive and print the response from the server until there is no more data
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketvar:
    socketvar.connect((inputted_url.host, 80))
    cmd = f"GET {inputted_url} HTTP/1.0\r\n\r\n".encode()
    socketvar.send(cmd)

    while True:
        data = socketvar.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")


# used openai chatgpt to automatically add verbose comments to the code, very impressive
=======
import os
import re
import sys
from datetime import datetime

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

if __name__ == "__main__":
    count = 0
    file = "mbox.txt"
    fpath = recurse_dir_search(file)
    inp = input("Enter a regular expression: ")
    targetpattern = re.compile(inp)
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.search(line):
                count += 1
    print(f"{file} had {count} lines that matched {inp}")
>>>>>>> f5d57a16bbcb2ad40a0c7659f51397f0e8458507
