import os

# from Module7.exercise2 import recurse_dir_search

print(os.listdir(os.getcwd()))

# fname = input("Enter file name: ")
# path = recurse_dir_search(fname, os.path.dirname(os.path.abspath(__file__)))
# fh = open(fname)
# wordset = set()
# for line in fh:
#     line = line.rstrip().split()
#     for word in line:
#         wordset.add(word)
# print(sorted(wordset))
