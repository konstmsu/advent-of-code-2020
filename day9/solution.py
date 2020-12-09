# %%

import numpy as np


def solve1(preambleSize, lines):
    numbers = [int(line) for line in lines]

    lastN = set(numbers[:preambleSize])

    def findSum(number):
        nonlocal lastN
        for a in lastN:
            if (number - a) in lastN:
                return a, number - a

    for i in range(preambleSize, len(numbers)):
        number = numbers[i]
        sumOf = findSum(number)

        if sumOf is None:
            return number

        lastN.remove(numbers[i - preambleSize])
        lastN.add(number)

    raise Exception()


def solve2(targetSum, lines):
    numbers = [int(line) for line in lines]
    n = len(lines)

    sums = np.zeros((n + 1, n + 1), dtype=np.int)
    for i in range(n):
        for j in range(i, n):
            sums[i + 1, j + 1] = sums[i + 1, j] + numbers[j]

    for r, c in np.argwhere(sums == targetSum):
        nn = numbers[r - 1 : c]
        return min(nn) + max(nn)

    raise Exception()


example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576""".splitlines()


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


with open("input.txt") as file:
    lines = file.read().splitlines()

expect(127, solve1(5, example))
expect(556543474, solve1(25, lines))

expect(62, solve2(127, example))
expect(76096372, solve2(556543474, lines))
