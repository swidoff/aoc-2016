from collections import Counter
from typing import List


def read_input() -> List[str]:
    with open("../input/day6.txt") as f:
        return f.readlines()


def part1(codes: List[str]) -> str:
    return "".join(Counter(code[i] for code in codes).most_common(1)[0][0] for i in range(0, len(codes[0])))


def least_common(counter: Counter) -> str:
    return min(counter.items(), key=lambda p: p[1])[0]


def part2(codes: List[str]) -> str:
    return "".join(least_common(Counter(code[i] for code in codes)) for i in range(0, len(codes[0])))


example = """eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar"""


def test_part1_example():
    assert part1(example.split("\n")) == "easter"


def test_part1():
    print(part1(read_input()))


def test_part2_example():
    assert part2(example.split("\n")) == "advent"


def test_part2():
    print(part2(read_input()))
