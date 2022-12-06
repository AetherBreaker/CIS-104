count = {}


if __name__ == "__main__":
    fpath = "mbox-short.txt"
    with open(fpath) as fhand:
        for line in fhand:
            if line.startswith("From "):
                line = line.strip().split()
                hour = line[5].split(":")[0]
                count[f"{hour:0>2}"] = count.get(f"{hour:0>2}", 0) + 1

    print(
        "\n".join(
            f"{hour} {count}"
            for hour, count in sorted(
                ((hour, count) for hour, count in count.items()),
                key=lambda x: int(x[0]),
            )
        )
    )
