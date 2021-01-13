import re
from collections import deque
from typing import List

from src.day12 import assembunny


def read_input(file: str = "day24.txt") -> List[str]:
    with open(f"../input/{file}") as f:
        return f.readlines()


def bfs(grid: List[str], return_to_zero: bool = False) -> int:
    start_r, start_c = -1, -1
    numbers = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "0":
                start_r = r
                start_c = c
            elif grid[r][c].isdigit():
                numbers += 1

    initial_state = (start_r, start_c, 0)
    seen = {initial_state}
    q = deque()
    q.append((initial_state, 0))

    while q:
        (r, c, collected), steps = q.popleft()
        for rd, cd in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            new_r, new_c = r + rd, c + cd
            if 0 <= new_r < len(grid) and 0 <= new_c <= len(grid[new_r]) and grid[new_r][new_c] != "#":
                new_collected = collected
                if grid[new_r][new_c].isdigit():
                    number = int(grid[new_r][new_c])
                    if number > 0:
                        new_collected |= 1 << number - 1

                new_state = (new_r, new_c, new_collected)
                if bin(new_collected).count("1") == numbers and (
                    not return_to_zero or new_r == start_r and new_c == start_c
                ):
                    return steps + 1
                elif new_state not in seen:
                    seen.add(new_state)
                    q.append((new_state, steps + 1))

    return -1


def test_part1_example():
    example = """###########
#0.1.....2#
#.#######.#
#4.......3#
###########"""
    assert bfs(example.splitlines()) == 14


def test_part1():
    assert bfs(read_input()) == 490


def test_part2():
    print(bfs(read_input(), return_to_zero=True))
