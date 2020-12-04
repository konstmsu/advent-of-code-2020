# %%

from typing import List


def solve1(lines: List[str]):
    required = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    currentPassport = {}

    validCount = 0

    def endPassport():
        nonlocal currentPassport, validCount
        if len(required - currentPassport.keys()) == 0:
            validCount += 1

        currentPassport = {}

    for line in lines:
        if line == "":
            endPassport()
        else:
            for pair in line.split(" "):
                print(pair)
                k, v = pair.split(":")
                currentPassport[k] = v

    endPassport()

    return validCount


with open("input.txt") as file:
    lines = file.read().splitlines()

print(solve1(lines))