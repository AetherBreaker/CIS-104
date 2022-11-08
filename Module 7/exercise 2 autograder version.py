"""This detects whether this python module is being ran as a script, or being imported
if it is being ran directly, the builtin __name__ variable will equal "__main__" otherwise
if the module has been imported, __name__ will equal the name of the module.

This allows you to run this file as a script, while still allowing you to import the recurse_dir_search
func for use in other python modules without accidentally running the script below.
"""
if __name__ == "__main__":

    uinput = input("Enter a file name:")

    total, count = 0, 0.0
    with open(uinput, "r") as file:
        for line in file:
            if not line.startswith("X-DSPAM-Confidence:"):
                continue
            line = line.strip().partition(" ")
            total += float(line[2])
            count += 1
    print(f"Average spam confidence: {total/count}")
