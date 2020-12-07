# %%

from typing import List


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


def valueOrEmpty(dict, key):
    return dict[key] if key in dict else []


def addToList(dict, key, value):
    if key not in dict:
        dict[key] = []
    dict[key].append(value)


def parse(lines: List[str]) -> int:
    parents = {}
    children = {}

    def addRelation(parent, child, count):
        addToList(parents, child, parent)
        addToList(children, parent, (child, count))

    for line in lines:
        container, contents = line.split(" bags contain ")
        if contents == "no other bags.":
            continue
        for content in contents.split(", "):
            count, color1, color2, _ = content.split(" ")
            addRelation(container, f"{color1} {color2}", int(count))

    return parents, children


def solve1(lines: List[str]) -> int:
    parents, _ = parse(lines)

    toVisit = ["shiny gold"]
    ancestors = set()

    while toVisit:
        bag = toVisit.pop()
        ancestors.add(bag)
        toVisit += valueOrEmpty(parents, bag)

    return len(ancestors) - 1


def solve2(lines: List[str]) -> int:
    _, children = parse(lines)

    def countDescendants(root):
        nonlocal children
        return 1 + sum(
            countDescendants(child) * count
            for child, count in valueOrEmpty(children, root)
        )

    return countDescendants("shiny gold") - 1


with open("input.txt") as file:
    lines = file.read().splitlines()

example1 = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.""".splitlines()

example2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.""".splitlines()

expect(4, solve1(example1))
expect(248, solve1(lines))
expect(32, solve2(example1))
expect(126, solve2(example2))

print(f"{solve1(lines)=}")
print(f"{solve2(lines)=}")

expect(57281, solve2(lines))
