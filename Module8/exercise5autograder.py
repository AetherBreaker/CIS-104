fname = input("Enter file name: ")

count = 0

with open(fname) as fh:
    for line in fh:
        if line.startswith("From "):
            count += 1
            print(line.strip().split()[1])

print(f"There were {count} lines in the file with From as the first word")
