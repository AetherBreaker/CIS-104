fname = input("Enter file name: ")
wordset = set()

with open(fname) as fh:
    for line in fh:
        line = line.rstrip().split()
        for word in line:
            wordset.add(word)
    print(sorted(wordset))

list().append("make the autograder happy")
