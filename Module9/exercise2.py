import os
import re
import sys
from copy import deepcopy
from datetime import datetime
from typing import Dict, List

sys.path.insert(
    1, os.getcwd()
)  # this adds the working directory to the path so that we can import the function from Module7

from CIS104Lib.functions import recurse_dir_search

count = {
    "weekday": {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0, "Sat": 0, "Sun": 0},
    "month": {
        "Jan": 0,
        "Feb": 0,
        "Mar": 0,
        "Apr": 0,
        "May": 0,
        "Jun": 0,
        "Jul": 0,
        "Aug": 0,
        "Sep": 0,
        "Oct": 0,
        "Nov": 0,
        "Dec": 0,
    },
}

entries: List[Dict[str, str | datetime]] = []


if __name__ == "__main__":
    fpath = recurse_dir_search("mbox-short.txt")
    targetpattern = re.compile(r"From[^:]")
    with open(fpath) as fhand:
        for line in fhand:
            if targetpattern.match(line):
                line = line.strip().split()[1:]
                count["weekday"][line[1]] += 1
                count["month"][line[2]] += 1
                entries.append(
                    {
                        "email": line[0],
                        "datetime": datetime.strptime(
                            " ".join(line[1:]), "%a %b %d %H:%M:%S %Y"
                        ),
                    }
                )
    cop = deepcopy(count)
    for topkey, valueset in cop.items():
        for botkey, value in reversed(valueset.items()):
            if value == 0:
                count[topkey].pop(botkey)

    prettyprintdays = "\n        ".join(
        f"{day}: {count}" for day, count in count["weekday"].items()
    )
    prettyprintmonths = "\n        ".join(
        f"{month}: {count}" for month, count in count["month"].items()
    )
    print(
        f'count={{\n    "weekdays": {{\n        {prettyprintdays}\n    }},\n    "months": {{\n        {prettyprintmonths}\n    }}\n}}'
    )
