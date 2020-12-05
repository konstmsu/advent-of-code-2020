# %%


def parsePart(part):
    v = 0

    for d in part:
        v = v * 2 + (d in "BR")

    return v


def parse(boardingPass):
    row = parsePart(boardingPass[:7])
    column = parsePart(boardingPass[-3:])
    return {"row": row, "column": column, "seatID": row * 8 + column}


def expect(expected, actual):
    if expected != actual:
        raise Exception(f"{expected=} {actual=}")


expect(0, parsePart("FF"))
expect(1, parsePart("FB"))
expect(2, parsePart("BF"))
expect(3, parsePart("BB"))

expect({"row": 70, "column": 7, "seatID": 567}, parse("BFFFBBFRRR"))
expect({"row": 14, "column": 7, "seatID": 119}, parse("FFFBBBFRRR"))
expect({"row": 102, "column": 4, "seatID": 820}, parse("BBFFBBFRLL"))

with open("input.txt") as file:
    lines = file.read().splitlines()

ids = [int(parse(v)["seatID"]) for v in lines]

print(max(ids))
print(set(range(min(ids), max(ids) + 1)).difference(ids))
