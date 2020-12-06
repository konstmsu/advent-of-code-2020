# %%

from itertools import *
from more_itertools import *

with open("input.txt") as file:
    lines = file.read()

groups = [[set(p) for p in g.split("\n")] for g in lines.strip().split("\n\n")]


def solve1(groups):
    return sum(len(last(accumulate(g, set.union))) for g in groups)


def solve2(groups):
    return sum(len(last(accumulate(g, set.intersection))) for g in groups)


print(f"{solve1(groups)=}")
print(f"{solve2(groups)=}")

assert 6903 == solve1(groups)
assert 3493 == solve2(groups)
