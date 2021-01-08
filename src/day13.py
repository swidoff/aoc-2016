from collections import deque


def is_open(x: int, y: int, key: int) -> bool:
    v = x * x + 3 * x + 2 * x * y + y + y * y + key
    return sum(int(d) for d in bin(v)[2:]) % 2 == 0


def part1(start_x: int, start_y: int, end_x: int, end_y: int, key: int) -> int:
    q = deque()
    seen = {(start_x, start_y)}
    q.append((start_x, start_y, 0))

    while q:
        x, y, steps = q.popleft()
        new_steps = steps + 1
        for xd, yd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x + xd, y + yd
            if new_x > 0 and new_y > 0 and (new_x, new_y) not in seen and is_open(new_x, new_y, key):
                if new_x == end_x and new_y == end_y:
                    return new_steps
                else:
                    seen.add((new_x, new_y))
                    q.append((new_x, new_y, new_steps))

    return -1


def part2(start_x: int, start_y: int, max_steps: int, key: int) -> int:
    q = deque()
    seen = {(start_x, start_y)}
    q.append((start_x, start_y, 0))

    while q:
        x, y, steps = q.popleft()
        if steps == max_steps:
            continue

        new_steps = steps + 1
        for xd, yd in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_x, new_y = x + xd, y + yd
            if new_x >= 0 and new_y >= 0 and (new_x, new_y) not in seen and is_open(new_x, new_y, key):
                seen.add((new_x, new_y))
                q.append((new_x, new_y, new_steps))

    return len(seen)


def test_part1_example():
    assert part1(1, 1, 7, 4, 10) == 11


def test_part1():
    print(part1(1, 1, 31, 39, 1358))


def test_part2():
    print(part2(1, 1, 50, 1358))
