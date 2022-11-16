from statistics import mean

numlist = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        numlist.append(int(num))
    except ValueError:
        print("Invalid input")
        continue
padding = 9
print(
    f"{'Total:':{padding}}{sum(numlist)}\n"
    f"{'Count:':{padding}}{len(numlist)}\n"
    f"{'Average:':{padding}}{mean(numlist)}\n"
)
