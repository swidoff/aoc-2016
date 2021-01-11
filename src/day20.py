from typing import List, Tuple


def read_input() -> List[str]:
    with open("../input/day20.txt") as f:
        return f.readlines()


def parse_input(lines: List[str]) -> List[Tuple[int, int]]:
    # noinspection PyTypeChecker
    return [tuple(int(p) for p in line.split("-")) for line in lines]


def part1(ranges: List[Tuple[int, int]], value: int = 0) -> int:
    contain_value, next_ranges = [], []
    for rng in ranges:
        if rng[0] <= value <= rng[1]:
            contain_value.append(rng)
        else:
            next_ranges.append(rng)

    if contain_value:
        next_value = max(rng[1] for rng in contain_value) + 1
        return part1(next_ranges, next_value)
    else:
        return value


def part2(start_ranges: List[Tuple[int, int]], start_value: int = 0, max_value: int = 4294967295) -> int:
    ranges = start_ranges
    value = start_value
    count = 0
    while ranges:
        contain_value, next_ranges = [], []
        for rng in ranges:
            if rng[0] <= value <= rng[1]:
                contain_value.append(rng)
            elif value <= rng[1]:
                next_ranges.append(rng)

        if contain_value:
            next_value = max(rng[1] for rng in contain_value) + 1
            value = next_value
        elif next_ranges:
            next_value = min(rng[0] for rng in next_ranges)
            count += next_value - value
            value = next_value

        ranges = next_ranges

    return count + (max_value - value + 1)


def test_part1_examples():
    assert part1([(5, 8), (0, 2), (4, 7)]) == 3
    assert part1([(5, 8), (0, 3), (4, 7)]) == 9


def test_part1():
    print(part1(parse_input(read_input())))


def test_part2_examples():
    assert part2([(5, 8), (0, 2), (4, 7)], max_value=9) == 2
    assert part2([(5, 8), (0, 3), (4, 7)], max_value=9) == 1


def test_part2():
    print(part2(parse_input(read_input())))
