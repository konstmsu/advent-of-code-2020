# %%
import numpy as np


def solve1(target: int, count: int, numbers: List[int]) -> int:
    nn = np.array(numbers)
    sums2 = nn.T + nn
    print(sums2 == target)


with open("input.txt") as file:
    numbers = [int(line) for line in file.readlines()]

print(solve1(2020, 2, set(), numbers))
