import re

text = "X-DSPAM-Confidence:    0.8475"

try:
    newstr = float(re.sub(r"[^0-9\.]", "", text))
except ValueError:
    print("Couldn't convert to float")
print(newstr)
