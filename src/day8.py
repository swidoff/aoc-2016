from typing import List
import re


def read_input() -> List[str]:
    with open("../input/day8.txt") as f:
        return f.readlines()


def execute(instructions: List[str], rows: int, cols: int) -> List[List[int]]:
    screen = [[0 for _ in range(cols)] for _ in range(rows)]

    for instruction in instructions:
        if match := re.match(r"rect (\d+)x(\d+)", instruction):
            w = int(match.group(1))
            h = int(match.group(2))
            for r in range(h):
                for c in range(w):
                    screen[r][c] = 1
        elif match := re.match(r"rotate row y=(\d+) by (\d+)", instruction):
            row = int(match.group(1))
            inc = int(match.group(2))
            for _ in range(inc):
                last = screen[row][-1]
                for c in reversed(range(cols)):
                    screen[row][c] = screen[row][c - 1]
                screen[row][0] = last
        elif match := re.match(r"rotate column x=(\d+) by (\d+)", instruction):
            col = int(match.group(1))
            inc = int(match.group(2))
            for _ in range(inc):
                last = screen[-1][col]
                for r in reversed(range(rows)):
                    screen[r][col] = screen[r - 1][col]
                screen[0][col] = last
        else:
            raise Exception("Unknown instruction", instruction)

    return screen


def print_screen(screen: List[List[int]]) -> str:
    return "\n".join("".join("#" if c == 1 else "." for c in row) for row in screen)


def test_part1_examples():
    assert print_screen(execute(["rect 3x2"], 3, 7)) == """###....\n###....\n......."""
    assert print_screen(execute(["rect 3x2", "rotate column x=1 by 1"], 3, 7)) == """#.#....\n###....\n.#....."""
    assert (
        print_screen(execute(["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4"], 3, 7))
        == """....#.#\n###....\n.#....."""
    )
    assert (
        print_screen(
            execute(["rect 3x2", "rotate column x=1 by 1", "rotate row y=0 by 4", "rotate column x=1 by 1"], 3, 7)
        )
        == """.#..#.#\n#.#....\n.#....."""
    )


def test_part1():
    screen = execute(read_input(), 6, 50)
    print(sum(c for row in screen for c in row))


def test_part2():
    screen = execute(read_input(), 6, 50)
    print()
    print(print_screen(screen))
