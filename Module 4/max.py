from random import randint
from typing import Iterable, Union


def myMax(*args: Union[str, int, bool]):
    newArgs = []
    for item in args:
        if isinstance(args[0], Iterable) and not (
            isinstance(args[0], str) or issubclass(args[0].__class__, str)
        ):
            newArgs.extend(item)
        else:
            newArgs.append(item)
    args = newArgs
    maxHolder = args[0]
    for item in args:
        if item > maxHolder:
            maxHolder = item
    return maxHolder


print(f"{myMax(1, 2, 3, 5, 1123, 2161)=}")

print(f'{myMax("15", "12351", "asdgasdg", "asiduyvha,m")=}')
numlist = []

for num in range(randint(3, 20)):
    numlist.append(randint(0, 100))
print(f"{numlist=}")
print(myMax(numlist))
