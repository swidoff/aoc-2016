from typing import List, Iterator, Tuple


def read_input() -> str:
    with open("../input/day1.txt") as f:
        return f.readline()


def parse(line) -> List[str]:
    return [step for step in line.split(", ")]


offsets = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def follow(steps: List[str]) -> Iterator[Tuple[int, int]]:
    x, y = 0, 0
    offset_index = 0
    for step in steps:
        if step[0] == "L":
            offset_index = abs((offset_index - 1) % len(offsets))
        elif step[0] == "R":
            offset_index = (offset_index + 1) % len(offsets)

        amount = int(step[1:])
        for _ in range(0, amount):
            x += offsets[offset_index][0]
            y += offsets[offset_index][1]
            yield x, y


def part1(steps: List[str]) -> int:
    x, y = 0, 0
    for step in follow(steps):
        x, y = step

    return abs(x) + abs(y)


def part2(steps: List[str]) -> int:
    pos = set()
    for step in follow(steps):
        if step in pos:
            x, y = step
            return abs(x) + abs(y)
        else:
            pos.add(step)

    return -1


def test_part1_examples():
    assert 5 == part1(["R2", "L3"])
    assert 2 == part1(["R2", "R2", "R2"])
    assert 12 == part1(parse("R5, L5, R5, R3"))


def test_part1():
    res = part1(parse(read_input()))
    print(res)
    assert res == 262


def test_part2_examples():
    assert 4 == part2(parse("R8, R4, R4, R8"))


def test_part2():
    print(part2(parse(read_input())))
    assert 131 == part2(parse(read_input()))
