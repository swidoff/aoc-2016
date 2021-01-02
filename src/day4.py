from collections import Counter
from dataclasses import dataclass
from typing import List
import re


def read_input() -> List[str]:
    with open("../input/day4.txt") as f:
        return f.readlines()


@dataclass(frozen=True)
class Code:
    name: str
    sector: int
    checksum: str

    def is_real(self) -> bool:
        counter = Counter(c for c in self.name if c != "-")
        most_common = [(-c, l) for (l, c) in counter.items()]
        actual_checksum = "".join(l for _, l in sorted(most_common))[0:5]
        return self.checksum == actual_checksum

    def decrypt(self) -> str:
        def decypt_letter(c: str) -> str:
            if c == "-":
                return " "
            else:
                return chr((ord(c) - ord("a") + self.sector) % 26 + ord("a"))

        return "".join(decypt_letter(c) for c in self.name)


def parse(code: str) -> Code:
    m = re.match(r"([a-z-]+)-(\d+)\[(\w+)]", code)
    return Code(m.group(1), int(m.group(2)), m.group(3))


def test_part1_examples():
    assert parse("aaaaa-bbb-z-y-x-123[abxyz]").is_real()
    assert parse("aaaaa-bbb-z-y-x-123[abxyz]").is_real()
    assert parse("not-a-real-room-404[oarel]").is_real()
    assert not parse("totally-real-room-200[decoy]").is_real()


def test_part1():
    res = sum(code.sector for line in read_input() if (code := parse(line)).is_real())
    print(res)


def test_part1_example2():
    assert "very encrypted name" == parse("qzmt-zixmtkozy-ivhz-343[a]").decrypt()


def test_part2():
    for line in read_input():
        code = parse(line)
        if code.is_real():
            print(code.decrypt(), code.sector)
