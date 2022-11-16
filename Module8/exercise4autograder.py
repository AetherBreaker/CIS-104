fname = input("Enter file name: ")
fh = open(fname)
wordset = set()
for line in fh:
    line = line.rstrip().split()
    for word in line:
        wordset.add(word)
print(sorted(wordset))
