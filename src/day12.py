from typing import List
import re


def read_input() -> List[str]:
    with open("../input/day12.txt") as f:
        return f.readlines()


def evaluate(instructions: List[str], c: int = 0) -> int:
    reg = {
        "a": 0,
        "b": 0,
        "c": c,
        "d": 0,
    }
    pc = 0
    while pc < len(instructions):
        instruction = instructions[pc]
        pc_offset = assembunny(instruction, reg)
        pc += pc_offset

    return reg["a"]


def assembunny(instruction, reg):
    pc_offset = 1
    if match := re.match(r"cpy (-?\d+) (\w)", instruction):
        reg[match.group(2)] = int(match.group(1))
    elif match := re.match(r"cpy (\w) (\w)", instruction):
        reg[match.group(2)] = reg[match.group(1)]
    elif match := re.match(r"inc (\w)", instruction):
        reg[match.group(1)] += 1
    elif match := re.match(r"dec (\w)", instruction):
        reg[match.group(1)] -= 1
    elif match := re.match(r"jnz (\w|-?\d+) (\w|-?\d+)", instruction):
        cond = reg[match.group(1)] if match.group(1) in reg else int(match.group(1))
        offset = reg[match.group(2)] if match.group(2) in reg else int(match.group(2))
        if cond:
            pc_offset = offset
    return pc_offset


def test_part1_example():
    instructions = """cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a"""
    assert evaluate(instructions.splitlines()) == 42


def test_part1():
    print(evaluate(read_input()))


def test_part2():
    print(evaluate(read_input(), c=1))
