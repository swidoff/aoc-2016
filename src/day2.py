from typing import List, Iterator, Mapping, Tuple


def read_input() -> List[str]:
    with open("../input/day2.txt") as f:
        return f.readlines()


part1_pad = {
    (0, 0): "1",
    (0, 1): "2",
    (0, 2): "3",
    (1, 0): "4",
    (1, 1): "5",
    (1, 2): "6",
    (2, 0): "7",
    (2, 1): "8",
    (2, 2): "9",
}


def buttons_for(lines: List[str], pad: Mapping[Tuple[int, int], str], row_start: int, col_start: int) -> Iterator[str]:
    row, col = row_start, col_start
    for line in lines:
        for c in line:
            new_row, new_col = row, col
            if c == "U":
                new_row -= 1
            elif c == "L":
                new_col -= 1
            elif c == "D":
                new_row += 1
            elif c == "R":
                new_col += 1

            if (new_row, new_col) in pad:
                row, col = new_row, new_col

        yield pad[(row, col)]


def part1(lines: List[str]) -> str:
    return "".join(buttons_for(lines, part1_pad, 1, 1))


part2_pad = {
    (0, 2): "1",
    (1, 1): "2",
    (1, 2): "3",
    (1, 3): "4",
    (2, 0): "5",
    (2, 1): "6",
    (2, 2): "7",
    (2, 3): "8",
    (2, 4): "9",
    (3, 1): "A",
    (3, 2): "B",
    (3, 3): "C",
    (4, 2): "D",
}


def part2(lines: List[str]) -> str:
    return "".join(buttons_for(lines, part2_pad, 2, 0))


def test_part1_example():
    assert (
        part1(
            """ULL
RRDDD
LURDL
UUUUD""".split(
                "\n"
            )
        )
        == "1985"
    )


def test_part1():
    assert "36629" == part1(read_input())


def test_part2_example():
    assert (
        part2(
            """ULL
RRDDD
LURDL
UUUUD""".split(
                "\n"
            )
        )
        == "5DB3"
    )


def test_part2():
    res = part2(read_input())
    print(res)
    assert "99C3D" == res
