from typing import List, Tuple
import re


def read_input() -> List[str]:
    with open("../input/day21.txt") as f:
        return f.readlines()


def part1(initial: str, instructions: List[str]) -> str:
    code = [c for c in initial]
    for instruction in instructions:
        code = process_instruction(code, instruction)

    return "".join(code)


def process_instruction(code: List[str], instruction: str):
    if match := re.match(r"swap position (\d) with position (\d)", instruction):
        i, j = int(match.group(1)), int(match.group(2))
        tmp = code[i]
        code[i] = code[j]
        code[j] = tmp
    elif match := re.match(r"swap letter (\w) with letter (\w)", instruction):
        i = code.index(match.group(1))
        j = code.index(match.group(2))
        tmp = code[i]
        code[i] = code[j]
        code[j] = tmp
    elif match := re.match(r"rotate left (\d) steps?", instruction):
        i = int(match.group(1)) % len(code)
        code = code[i:] + code[:i]
    elif match := re.match(r"rotate right (\d) steps?", instruction):
        i = (len(code) - int(match.group(1))) % len(code)
        code = code[i:] + code[:i]
    elif match := re.match(r"rotate based on position of letter (\w)", instruction):
        index = code.index(match.group(1))
        steps = index + (2 if index >= 4 else 1)
        i = len(code) - steps
        code = code[i:] + code[:i]
    elif match := re.match(r"reverse positions (\d) through (\d)", instruction):
        i = int(match.group(1))
        j = int(match.group(2))
        code = code[:i] + list(reversed(code[i: j + 1])) + code[j + 1:]
    elif match := re.match(r"move position (\d) to position (\d)", instruction):
        i = int(match.group(1))
        j = int(match.group(2))
        tmp = code[i]
        del code[i]
        code.insert(j, tmp)

    return code


def part2(initial: str, instructions: List[str]) -> str:
    code = [c for c in initial]
    for instruction in instructions:
        if instruction.startswith("rotate left"):
            new_instruction = instruction.replace("left", "right")
        elif instruction.startswith("rotate right"):
            new_instruction = instruction.replace("right", "left")
        elif match := re.match(r"rotate based on position of letter (\w)", instruction):
            index = code.index(match.group(1))
            # Only works for the solution.
            lookup = {
                1: 1,
                3: 2,
                5: 3,
                7: 4,
                2: 6,
                4: 7,
                6: 8,
                0: 9,
            }
            new_instruction = f"rotate left {lookup[index]} steps"
        elif match := re.match(r"move position (\d) to position (\d)", instruction):
            i = int(match.group(1))
            j = int(match.group(2))
            new_instruction = f"move position {j} to position {i}"
        else:
            new_instruction = instruction

        code = process_instruction(code, new_instruction)

    return "".join(code)


def test_part1_example():
    instructions = [
        "swap position 4 with position 0",
        "swap letter d with letter b",
        "reverse positions 0 through 4",
        "rotate left 1 step",
        "move position 1 to position 4",
        "move position 3 to position 0",
        "rotate based on position of letter b",
        "rotate based on position of letter d",
    ]
    assert part1("abcde", instructions) == "decab"


def test_part1():
    print(part1("abcdefgh", read_input()))


def test_part2_example():
    instructions = [
        "swap position 4 with position 0",
        "swap letter d with letter b",
        "reverse positions 0 through 4",
        "rotate left 1 step",
        "move position 1 to position 4",
        "move position 3 to position 0",
        "rotate based on position of letter b",
        "rotate based on position of letter d",
    ]
    assert part2("decab", list(reversed(instructions))) == "abcde"


def test_part2():
    print(part2("fbgdceah", reversed(read_input())))