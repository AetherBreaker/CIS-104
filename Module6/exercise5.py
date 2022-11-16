text = "X-DSPAM-Confidence:    0.8475"

try:
    newstr = float(text[text.find("0") :])
except ValueError:
    print("Couldn't convert to float")
print(newstr)
