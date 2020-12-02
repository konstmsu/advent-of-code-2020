# %%

from typing import List


def solve1(lines: List[str]) -> int:
    validCount = 0

    for line in lines:
        template, password = line.split(": ")
        minMax, letter = template.split(" ")
        atLeast, atMax = [int(v) for v in minMax.split("-")]
        matches = password.count(letter)
        if atLeast <= matches <= atMax:
            validCount += 1

    return validCount


def solve2(lines: List[str]) -> int:
    validCount = 0

    for line in lines:
        template, password = line.split(": ")
        minMax, letter = template.split(" ")
        p1, p2 = [int(v) - 1 for v in minMax.split("-")]
        if (password[p1] == letter) + (password[p2] == letter) == 1:
            validCount += 1

    return validCount


with open("input.txt") as file:
    lines = file.readlines()

print(solve1(lines))
print(solve2(lines))