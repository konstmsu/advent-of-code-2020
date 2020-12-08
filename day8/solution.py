# %%


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


class Handheld:
    def __init__(self, lines):
        self.program = [((p := line.split(" "))[0], int(p[1])) for line in lines]
        self.acc = 0
        self.cpu = 0
        self.visited = set()
        self.commands = {
            "acc": lambda arg: (self.acc + arg, self.cpu + 1),
            "nop": lambda arg: (self.acc, self.cpu + 1),
            "jmp": lambda arg: (self.acc, self.cpu + arg),
        }

    def step(self):
        self.visited.add(self.cpu)
        op, arg = self.program[self.cpu]
        self.acc, self.cpu = self.commands[op](arg)

    def isInfiniteLoopDetected(self):
        return self.cpu in self.visited

    def isTerminated(self):
        return self.cpu == len(self.program)


def getLoopAcc(lines):
    handheld = Handheld(lines)

    for i in range(100000):
        if handheld.isInfiniteLoopDetected():
            return handheld.acc
        handheld.step()

    raise Exception("No infinite loop detected")


def fixJumpNop(lines):
    for i in range(len(lines)):
        handheld = Handheld(lines)
        op, arg = handheld.program[i]
        if op == "acc":
            continue
        handheld.program[i] = ("nop" if op == "jmp" else "jmp"), arg
        for _ in range(10000):
            if handheld.isTerminated():
                return handheld.acc
            handheld.step()


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

expect(8, fixJumpNop(sample))
expect(1245, fixJumpNop(lines))