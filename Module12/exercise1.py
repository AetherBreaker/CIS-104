# Install the required modules `validators` and `yarl` by running
# `pip freeze > requirements.txt` in your terminal
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
