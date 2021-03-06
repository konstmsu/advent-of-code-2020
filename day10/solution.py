# %%


def solve1(lines):
    numbers = sorted([0] + [int(line) for line in lines])
    diffCounts = {}
    for n1, n2 in zip(numbers, numbers[1:]):
        diff = n2 - n1
        if diff not in diffCounts:
            diffCounts[diff] = 0

        diffCounts[diff] += 1

    diffCounts[3] += 1

    return diffCounts[1], diffCounts[3]


def solve2(lines):
    numbers = set(int(line) for line in lines)
    numbers.add(0)
    end = max(numbers) + 3
    cache = {0: 1}

    def countUp(fr):
        nonlocal numbers, cache

        if fr in cache:
            return cache[fr]

        ways = 0
        for i in range(1, 4):
            v = fr - i
            if v in numbers:
                ways += countUp(v)

        cache[fr] = ways
        return ways

    return countUp(end)


sample1 = """16
10
15
5
1
11
7
19
6
12
4""".splitlines()

sample2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3""".splitlines()


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


with open("input.txt") as file:
    lines = file.read().splitlines()

expect((7, 5), solve1(sample1))
expect((22, 10), solve1(sample2))
expect((70, 34), solve1(lines))
print(70 * 34)

expect(8, solve2(sample1))
expect(19208, solve2(sample2))
expect(48358655787008, solve2(lines))
