# %%
from typing import Set


def solve1(target: int, numbers: Set[int]) -> int:
    for n in numbers:
        if (target - n) in numbers:
            return (target - n) * n

    raise "Not found"


def solve2(target: int, numbers: Set[int]) -> int:
    for n1 in numbers:
        for n2 in numbers:
            n3 = target - n1 - n2
            if n3 in numbers:
                return n1 * n2 * n3

    raise "Not found"


with open("input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(f"{solve1(2020, set(numbers))=}")
print(f"{solve2(2020, set(numbers))=}")
