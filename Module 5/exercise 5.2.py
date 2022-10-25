largest = 1
smallest = 1
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
print("Maximum is", max(numlist))
print("Minimum is", min(numlist))
