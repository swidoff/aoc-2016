from typing import List, Tuple
import re


def read_input() -> List[str]:
    with open("../input/day15.txt") as f:
        return f.readlines()


def parse_input(lines: List[str]) -> List[Tuple[int, int]]:
    return [
        (int(match.group(1)), int(match.group(2)))
        for line in lines
        if (match := re.match(r"Disc #\d has (\d+) positions; at time=0, it is at position (\d+).", line)) is not None
    ]


def solve(discs: List[Tuple[int, int]]) -> int:
    period = 1
    t = 0
    for i, (positions, start) in enumerate(discs):
        while True:
            if (t + start + i + 1) % positions == 0:
                period *= positions
                break
            t += period
    return t


def test_part1_example():
    example = """Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
"""
    assert solve(parse_input(example.splitlines())) == 5


def test_part1():
    print(solve(parse_input(read_input())))


def test_part2():
    discs = parse_input(read_input())
    discs.append((11, 0))
    print(solve(discs))
