import argparse
import json
import os
from pathlib import Path
from random import randint

from dice import roll

small = ["small", "sml", "1", 1]
medium = ["medium", "med", "2", 2]
large = ["large", "lrg", "3", 3]
path = Path(os.path.join(os.getcwd(), "json", "cavedat.json"))
cavedat = {}
with open(path) as data:
    cavedat = json.load(data)


def interpet_input(input: str) -> int:
    if input.casefold() in small:
        return "Small"
    elif input.casefold() in medium:
        return "Medium"
    elif input.casefold() in large:
        return "Large"


parser = argparse.ArgumentParser(
    description=(
        f"Returns a random set of potential gems and ores to be "
        f"found within a cave based off cave size"
    )
)
parser.add_argument(
    "-s",
    type=interpet_input,
    default=["Small", "Medium", "Large"][randint(1, 3) - 1],
    help="Select a cave size, a size is randomly selected if option is omitted",
    required=False,
    dest="size",
)

args = parser.parse_args()
cave = cavedat["Cave Tables"][args.size]
table = list(cave.values())[randint(0, 1)]

outputlines = [f"Results for {args.size} cave:"]
for tier, count in table.items():
    outputlines.append(f"  {tier}:")
    tier = cavedat["Gem Tables"][tier]
    for item in range(count):
        units = roll(tier["Units"])[0]
        gem = tier["Table"][str(roll(f"1d{len(tier['Table'])}")[0])]
        outputlines.append(f"    {gem}: {units}")
print("\n".join(outputlines))
