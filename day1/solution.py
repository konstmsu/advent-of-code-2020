# %%
from typing import Set


def solve1(target: int, count: int, numbers: Set[int]) -> int:
    for n in numbers:
        if (target - n) in numbers:
            return (target - n) * n

    raise "Not found"


with open("input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(solve1(2020, 2, set(numbers)))
