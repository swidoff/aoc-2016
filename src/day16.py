def fill(a: str, length: int) -> str:
    b = a[-1::-1].translate({ord("0"): ord("1"), ord("1"): ord("0")})
    res = f"{a}0{b}"
    if len(res) >= length:
        return res[:length]
    else:
        return fill(res, length)


def checksum(a: str) -> str:
    res = "".join("1" if a[i : i + 2] in {"11", "00"} else "0" for i in range(0, len(a), 2))
    if len(res) % 2 == 1:
        return res
    else:
        return checksum(res)


def test_part1_examples():
    assert fill("1", 3) == "100"
    assert fill("0", 3) == "001"
    assert fill("11111", 11) == "11111000000"
    assert fill("111100001010", 25) == "1111000010100101011110000"
    assert checksum("110010110100") == "100"
    assert checksum(fill("10000", 20)) == "01100"


def test_part1():
    print(checksum(fill("01110110101001000", 272)))


def test_part2():
    print(checksum(fill("01110110101001000", 35651584)))
