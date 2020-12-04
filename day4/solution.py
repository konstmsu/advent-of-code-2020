# %%

from typing import List
import re


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
                k, v = pair.split(":")
                currentPassport[k] = v

    endPassport()

    return validCount


validators = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: 150 <= int(v[:-2]) <= 193
    if v.endswith("cm")
    else 59 <= int(v[:-2]) <= 76
    if v.endswith("in")
    else False,
    "hcl": lambda v: re.match("^\\#[0-9a-f]{6}$", v),
    "ecl": lambda v: v
    in [
        "amb",
        "blu",
        "brn",
        "gry",
        "grn",
        "hzl",
        "oth",
    ],
    "pid": lambda v: re.match("^\\d{9}$", v),
}


def solve2(lines: List[str]):
    currentPassport = {}

    validCount = 0

    def endPassport():
        nonlocal currentPassport, validCount
        isValid = True

        if len(validators.keys() - currentPassport.keys()) > 0:
            isValid = False
        else:
            for k, v in currentPassport.items():
                if not validators[k](v):
                    print(f"{v} failed validator {k}")
                    isValid = False

        if isValid:
            validCount += 1

        currentPassport = {}

    for line in lines:
        if line == "":
            endPassport()
        else:
            for pair in line.split(" "):
                k, v = pair.split(":")
                if k == "cid":
                    continue
                currentPassport[k] = v

    endPassport()

    return validCount


with open("input.txt") as file:
    lines = file.read().splitlines()

print(solve1(lines))

# 223 is too low
print(solve2(lines))
