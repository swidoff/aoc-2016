from collections import deque
from typing import List

from day5 import hash_hex

moves = [("U", -1, 0), ("D", 1, 0), ("L", 0, -1), ("R", 0, 1)]


def search(passcode: str, stop_at_shortest: bool = True) -> List[str]:
    q = deque()
    q.append(("", 0, 0))
    seen = {""}
    res = []

    while q:
        path, r, c = q.popleft()
        hashed_code = hash_hex((passcode + path).encode())

        for next_path, next_r, next_c in [
            (path + letter, r + rd, c + cd)
            for code_char, (letter, rd, cd) in zip(hashed_code, moves)
            if code_char >= "b"
        ]:
            if next_r == 3 and next_c == 3:
                res.append(next_path)
                if stop_at_shortest:
                    return res
            elif 0 <= next_r < 4 and 0 <= next_c < 4 and next_path not in seen:
                seen.add(next_path)
                q.append((next_path, next_r, next_c))

    return res


def shortest_path(passcode: str) -> str:
    paths = search(passcode)
    res = min(paths, key=lambda p: len(p))
    return res


def longest_path_len(passcode: str) -> int:
    paths = search(passcode, stop_at_shortest=False)
    res = max(paths, key=lambda p: len(p))
    return len(res)


def test_part1_examples():
    assert shortest_path("ihgpwlah") == "DDRRRD"
    assert shortest_path("kglvqrro") == "DDUDRLRRUDRD"
    assert shortest_path("ulqzkmiv") == "DRURDRUDDLLDLUURRDULRLDUUDDDRR"


def test_part1():
    print(shortest_path("veumntbg"))


def test_part2_examples():
    assert longest_path_len("ihgpwlah") == 370
    assert longest_path_len("kglvqrro") == 492
    assert longest_path_len("ulqzkmiv") == 830


def test_part2():
    print(longest_path_len("veumntbg"))

