import toolz


def next_tile(left, center, right) -> str:
    if left == "^" and center == "^" and right == ".":
        return "^"
    elif left == "." and center == "^" and right == "^":
        return "^"
    elif left == "^" and center == "." and right == ".":
        return "^"
    elif left == "." and center == "." and right == "^":
        return "^"
    else:
        return "."


def count_safe_tiles(start_line: str, rows: int) -> int:
    line = start_line
    count = 0
    for i in range(rows):
        count += sum(c == "." for c in line)
        if i < rows - 1:
            line = "".join(next_tile(*window) for window in toolz.sliding_window(3, "." + line + "."))

    return count


def test_part1_examples():
    assert count_safe_tiles(".^^.^.^^^^", 10) == 38


def test_part1():
    line = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
    print(count_safe_tiles(line, 40))


def test_part2():
    line = ".^^.^^^..^.^..^.^^.^^^^.^^.^^...^..^...^^^..^^...^..^^^^^^..^.^^^..^.^^^^.^^^.^...^^^.^^.^^^.^.^^.^."
    print(count_safe_tiles(line, 400000))
