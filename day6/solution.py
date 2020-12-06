# %%


def solve1(lines):
    currentGroup = set()
    groups = []

    def groupComplete():
        nonlocal currentGroup
        groups.append(len(currentGroup))
        currentGroup = set()
        print(f"{groups=}")

    for line in lines:
        if line == "":
            groupComplete()
        else:
            currentGroup = currentGroup.union(line)

    groupComplete()

    return sum(groups)


with open("input.txt") as file:
    lines = file.read().splitlines()

solve1(lines)