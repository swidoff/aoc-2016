import re


def read_input() -> str:
    with open("../input/day9.txt") as f:
        return f.readline().strip()


def decompress(input_str: str) -> str:
    current = input_str
    res = []
    while current:
        parts = re.split(r"(\(\d+x\d+\))", current, maxsplit=1)
        res.append(parts[0])

        if len(parts) == 1:
            current = ""
        else:
            sep, end = parts[1:]
            match = re.match(r"(\d+)x(\d+)", sep[1:-1])
            chars = int(match.group(1))
            rep = int(match.group(2))
            res.append(end[:chars] * rep)
            current = end[chars:]

    return "".join(res)


def decompress_v2(input_str: str) -> int:
    current = input_str
    res = 0
    while current:
        parts = re.split(r"(\(\d+x\d+\))", current, maxsplit=1)
        res += len(parts[0])

        if len(parts) == 1:
            current = ""
        else:
            sep, end = parts[1:]
            match = re.match(r"(\d+)x(\d+)", sep[1:-1])
            chars = int(match.group(1))
            rep = int(match.group(2))
            res += rep * decompress_v2(end[:chars])
            current = end[chars:]

    return res


def test_part1_examples():
    assert decompress("ADVENT") == "ADVENT"
    assert decompress("A(1x5)BC") == "ABBBBBC"
    assert decompress("(3x3)XYZ") == "XYZXYZXYZ"
    assert decompress("A(2x2)BCD(2x2)EFG") == "ABCBCDEFEFG"
    assert decompress("(6x1)(1x3)A") == "(1x3)A"
    assert decompress("X(8x2)(3x3)ABCY") == "X(3x3)ABC(3x3)ABCY"


def test_part1():
    print(len(decompress(read_input())))


def test_part2_examples():
    assert decompress_v2("(3x3)XYZ") == 9
    assert decompress_v2("X(8x2)(3x3)ABCY") == len("XABCABCABCABCABCABCY")
    assert decompress_v2("(27x12)(20x12)(13x14)(7x10)(1x12)A") == 241920
    assert decompress_v2("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN") == 445


def test_part2():
    print(decompress_v2(read_input()))
