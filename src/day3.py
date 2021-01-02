import re
from typing import List, Tuple


def read_input() -> List[str]:
    with open("../input/day3.txt") as f:
        return f.readlines()


def parse_part1(lines: List[str]) -> List[Tuple[int, ...]]:
    return [tuple(int(t.strip()) for t in re.split(r"\s+", line.strip())) for line in lines]


def parse_part2(lines: List[str]) -> List[Tuple[int, ...]]:
    bufs, res = [[], [], []], []
    for i, line in enumerate(lines):
        for j, n in enumerate(int(t.strip()) for t in re.split(r"\s+", line.strip())):
            bufs[j].append(n)

        if (i + 1) % 3 == 0:
            for buf in bufs:
                res.append(tuple(buf))
                buf.clear()

    return res


def is_valid_triangle(sides: Tuple[int, ...]) -> bool:
    return all(sides[s1] + sides[s2] > sides[s3] for (s1, s2, s3) in [(0, 1, 2), (0, 2, 1), (1, 2, 0)])


def test_part1_example():
    assert not is_valid_triangle((5, 10, 25))


def test_part1():
    res = sum(is_valid_triangle(t) for t in parse_part1(read_input()))
    print(res)


def test_part2():
    res = sum(is_valid_triangle(t) for t in parse_part2(read_input()))
    print(res)
