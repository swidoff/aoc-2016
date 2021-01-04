from dataclasses import dataclass
from functools import reduce
from typing import List, Set
import re

import toolz


def read_input() -> List[str]:
    with open("../input/day7.txt") as f:
        return f.readlines()


def has_abba(part: str) -> bool:
    return any(c1 == c4 and c2 == c3 and c1 != c2 for c1, c2, c3, c4 in toolz.sliding_window(4, part))


def find_aba(part: str) -> Set[str]:
    return set(f"{c1}{c2}{c3}" for c1, c2, c3 in toolz.sliding_window(3, part) if c1 == c3 and c2 != c3)


def to_bab(aba: str) -> str:
    return aba[1] + aba[0] + aba[1]


@dataclass
class Address:
    outside: List[str]
    inside: List[str]

    def is_tls(self) -> bool:
        return any(has_abba(part) for part in self.outside) and not any(has_abba(part) for part in self.inside)

    def is_ssl(self) -> bool:
        aba = reduce(lambda s, p: s | find_aba(p), self.outside, set())
        bab = reduce(lambda s, p: s | set(map(to_bab, find_aba(p))), self.inside, set())
        return len(aba & bab) > 0


def parse_address(addr: str) -> Address:
    parts = re.split(r"[]\[]", addr)
    return Address(parts[0::2], parts[1::2])


def part1(lines: List[str]) -> int:
    return sum(parse_address(line).is_tls() for line in lines)


def part2(lines: List[str]) -> int:
    return sum(parse_address(line).is_ssl() for line in lines)


def test_part1_examples():
    assert parse_address("abba[mnop]qrst").is_tls()
    assert not parse_address("abcd[bddb]xyyx").is_tls()
    assert not parse_address("aaaa[qwer]tyui").is_tls()
    assert parse_address("ioxxoj[asdfgh]zxcvbn").is_tls()


def test_part1():
    print(part1(read_input()))


def test_part2_examples():
    assert parse_address("aba[bab]xyz").is_ssl()
    assert not parse_address("xyx[xyx]xyx").is_ssl()
    assert parse_address("aaa[kek]eke").is_ssl()
    assert parse_address("zazbz[bzb]cdb").is_ssl()


def test_part2():
    print(part2(read_input()))
