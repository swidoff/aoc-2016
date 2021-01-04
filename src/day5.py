import hashlib
import toolz


def hash_hex(key: bytes) -> str:
    m = hashlib.md5()
    m.update(key)
    return m.digest().hex()


def part1(prefix: str, start: int = 0, end: int = 100000000) -> str:
    return "".join(
        toolz.take(
            8,
            (
                hash_value[5]
                for index in range(start, end)
                if (hash_value := hash_hex(f"{prefix}{index}".encode())).startswith("00000")
            ),
        )
    )


def part2(prefix: str, start: int = 0):
    digits = {}
    index = start
    while len(digits) < 8:
        hash_value = hash_hex(f"{prefix}{index}".encode())
        if hash_value.startswith("00000") and hash_value[5].isdigit():
            pos = int(hash_value[5])
            if pos < 8 and pos not in digits:
                digits[pos] = hash_value[6]

        index += 1

    res = [""] * 8
    for index, digit in digits.items():
        res[index] = digit

    return "".join(res)


def test_part1_example():
    assert part1("abc", start=3231929) == "18f47a30"


def test_part1():
    print(part1("reyedfim", start=0))


def test_part2_example():
    assert part2("abc", start=3231929) == "05ace8e3"


def test_part2():
    print(part2("reyedfim", start=0))
