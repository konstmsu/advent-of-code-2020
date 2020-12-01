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
            for n3 in numbers:
                # 3 nested loops for lulz
                if n1 + n2 + n3 == target and n1 != n2 and n1 != n3 and n2 != n3:
                    return n1 * n2 * n3

    raise "Not found"


with open("input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(f"{solve1(2020, set(numbers))=}")
print(f"{solve2(2020, set(numbers))=}")
