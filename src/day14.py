from collections import deque
from dataclasses import dataclass
from typing import Optional, Iterator

import toolz

from day5 import hash_hex


def run_of(key: str, size: int) -> Optional[str]:
    for window in toolz.sliding_window(size, key):
        if all(c == window[0] for c in window[1:]):
            return window[0]
    return None


@dataclass
class Key(object):
    index: int
    key: str
    digit: str
    valid: Optional[int] = None
    validating_key: Optional[str] = None


def key_indexes(salt: str, stretch: int = 0) -> Iterator[Key]:
    index = 0
    awaiting = deque()

    while True:
        key = hash_hex(f"{salt}{index}".encode())
        for _ in range(stretch):
            key = hash_hex(key.encode())

        for k in awaiting:
            if not k.valid and k.digit * 5 in key:
                k.valid = index
                k.validating_key = key

        if awaiting and index - awaiting[0].index == 1000:
            k = awaiting.popleft()
            if k.valid:
                yield k

        if digit := run_of(key, 3):
            awaiting.append(Key(index, key, digit))

        index += 1


def test_part1_examples():
    it = key_indexes("abc")
    ind = list(toolz.take(70, it))
    assert ind[0].index == 39
    assert ind[1].index == 92
    assert ind[63].index == 22728


def test_part1():
    it = key_indexes("yjdafjpo")
    ind = toolz.nth(63, it)
    print(ind.index)


def test_part2_examples():
    it = key_indexes("abc", stretch=2016)
    ind = list(toolz.take(70, it))
    assert ind[0].index == 10
    assert ind[63].index == 22551


def test_part2():
    it = key_indexes("yjdafjpo", stretch=2016)
    ind = toolz.nth(63, it)
    print(ind.index)
