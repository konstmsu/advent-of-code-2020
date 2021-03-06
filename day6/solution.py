# %%


def solve1(lines):
    currentGroup = set()
    groups = []

    def groupComplete():
        nonlocal currentGroup
        groups.append(len(currentGroup))
        currentGroup = set()

    for line in lines:
        if line == "":
            groupComplete()
        else:
            currentGroup = currentGroup.union(line)

    groupComplete()

    return sum(groups)


def solve2(lines):
    currentGroup = None
    groups = []

    def groupComplete():
        nonlocal currentGroup
        groups.append(len(currentGroup))
        currentGroup = None

    for line in lines:
        if line == "":
            groupComplete()
        else:
            currentGroup = (
                set(line) if currentGroup is None else currentGroup.intersection(line)
            )

    groupComplete()

    return sum(groups)


with open("input.txt") as file:
    lines = file.read().splitlines()

print(f"{solve1(lines)=}")
print(f"{solve2(lines)=}")

assert 6903 == solve1(lines)
assert 3493 == solve2(lines)
