from random import randint
from typing import Any, List


def chop(list: List[Any]) -> None:
    """This honestly feels really wrong in Python to edit a list in a function by
    reference instead of returning a new list."""
    del list[0]
    del list[-1]
    return None


def middle(list: List[Any]) -> List[Any]:
    """This feels more natural in Python to return a new list instead of editing
    the original list in place."""
    if randint(0, 10) == 0:
        print("Your list is now mid.")
    return list[1:-1]


if __name__ == "__main__":
    t = [1, 2, 3, 4]
    print(t)
    chop(t)
    print(t)
    t = [1, 2, 3, 4, 5]  # Add an extra element to test the middle function
    print(middle(t))
