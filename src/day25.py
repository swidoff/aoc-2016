import re
from typing import List, Iterator

import toolz
from future.moves import itertools

from src.day12 import assembunny


def read_input(file: str = "day25.txt") -> List[str]:
    with open(f"../input/{file}") as f:
        return f.readlines()


def evaluate(instructions: List[str], a: int = 0) -> Iterator[int]:
    reg = {
        "a": a,
        "b": 0,
        "c": 0,
        "d": 0,
    }
    pc = 0
    while 0 <= pc < len(instructions):
        pc_offset = 1
        instruction = instructions[pc]
        if match := re.match(r"out (\w)", instruction):
            yield reg[match.group(1)]
        else:
            pc_offset = assembunny(instruction, reg)

        pc += pc_offset


def is_clock(iterator: Iterator[int], matches: int = 100):
    expected = itertools.cycle([0, 1])
    return all(a == e for a, e in toolz.take(matches, zip(expected, iterator)))


def test_part1():
    instructions = read_input()
    for i in range(1000):
        clock = evaluate(instructions, a=i)
        if is_clock(clock):
            print(i)
            break

    print("Done!")
