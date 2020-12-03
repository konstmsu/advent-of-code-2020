# %%
import numpy as np


def solve1(lines, right, down):
    treeCount = 0

    x = 0
    for l in lines[::down]:
        line = l.strip()
        if line[x % len(line)] == "#":
            treeCount += 1
        x += right

    return treeCount


with open("input.txt") as file:
    lines = file.readlines()

# not 89
# not 101
# 151 is correct
print(solve1(lines, 3, 1))

params = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
trees = [solve1(lines, right, down) for right, down in params]
print(np.prod(trees))