# %%


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


def getLoopAcc(lines):
    program = [((p := line.split(" "))[0], int(p[1])) for line in lines]
    acc = 0
    cpu = 0
    commands = {
        "acc": lambda arg: (acc + arg, cpu + 1),
        "nop": lambda arg: (acc, cpu + 1),
        "jmp": lambda arg: (acc, cpu + arg),
    }
    visited = set()

    for i in range(100000):
        if cpu in visited:
            return acc
        visited.add(cpu)

        op, arg = program[cpu]
        acc, cpu = commands[op](arg)

    return None


with open("input.txt") as file:
    lines = file.read().splitlines()

sample = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".splitlines()

expect(5, getLoopAcc(sample))
expect(1420, getLoopAcc(lines))