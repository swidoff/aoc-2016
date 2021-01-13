import re
from typing import List

from src.day12 import assembunny


def read_input(file: str = "day23.txt") -> List[str]:
    with open(f"../input/{file}") as f:
        return f.readlines()


def evaluate(instructions: List[str], a: int = 0, c: int = 0) -> int:
    reg = {
        "a": a,
        "b": 0,
        "c": c,
        "d": 0,
    }
    pc = 0
    while 0 <= pc < len(instructions):
        instruction = instructions[pc]
        pc_offset = 1
        if match := re.match(r"tgl (\w)", instruction):
            grp = match.group(1)
            if grp in reg:
                offset = reg[grp]
            else:
                offset = int(grp)

            index = pc + offset
            if 0 <= index < len(instructions) and index != pc:
                instruction = toggle(instructions[index])
                instructions[index] = instruction
        elif match := re.match(r"mul (\w) (\w)", instruction):
            r1 = match.group(1)
            r2 = match.group(2)
            reg["a"] += reg[r1] * reg[r2]
        else:
            pc_offset = assembunny(instruction, reg)

        pc += pc_offset

    return reg["a"]


def toggle(instruction: str) -> str:
    replacements = {
        "dec": "inc",
        "inc": "dec",
        "tgl": "inc",
        "jnz": "cpy",
        "cpy": "jnz",
    }

    res = instruction
    for src, tgt in replacements.items():
        if instruction.startswith(src):
            res = instruction.replace(src, tgt)
            break

    return res


def test_part1_example():
    example = """cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a"""
    assert evaluate(example.splitlines()) == 3


def test_part1():
    print(evaluate(read_input(), a=7))


def test_part2():
    print(evaluate(read_input("day23-2.txt"), a=12))
