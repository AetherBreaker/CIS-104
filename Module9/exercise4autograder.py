count = {}


if __name__ == "__main__":
    with open("mbox-short.txt") as fhand:
        for line in fhand:
            if line.startswith("From "):
                user = line.strip().split()[1]
                if user not in count:
                    count[user] = 1
                else:
                    count[user] += 1
    print("{} {}".format(*max(count.items(), key=lambda x: x[1])))
