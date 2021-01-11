from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Elf:
    presents: int
    next: Optional[Elf]


def part1(num_elves: int) -> int:
    first_elf = 1
    period = 1
    while num_elves > 2:
        period *= 2
        if num_elves % 2 == 1:
            first_elf += period
        num_elves //= 2

    return first_elf


def part2(num_elves: int) -> int:
    elves = [True] * num_elves

    i = 0
    j = 0
    spaces = 0
    remaining = num_elves
    while remaining > 2:
        offset = remaining // 2

        while spaces < offset:
            j = (j + 1) % num_elves
            if elves[j]:
                spaces += 1
        elves[j] = False
        spaces -= 1

        i = (i + 1) % num_elves
        while not elves[i]:
            i = (i + 1) % num_elves
        spaces -= 1
        remaining -= 1

    return i + 1


def test_part1_examples():
    assert part1(5) == 3
    assert part1(11) == 7
    assert part1(21) == 11


def test_part1():
    print(part1(3017957))


def test_part2_examples():
    assert part2(5) == 2
    assert part2(11) == 2
    assert part2(21) == 15
    assert part2(1000) == 271
    assert part2(10000) == 3439


def test_part2():
    # 1841611 (too high)
    print(part2(3017957))
