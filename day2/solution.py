# %%

from typing import List


def solve(lines: List[str]) -> int:
    validCount = 0

    for line in lines:
        template, password = line.split(": ")
        minMax, letter = template.split(" ")
        atLeast, atMax = [int(v) for v in minMax.split("-")]
        matches = password.count(letter)
        if atLeast <= matches <= atMax:
            validCount += 1

    return validCount


with open("input.txt") as file:
    lines = file.readlines()

print(solve(lines))