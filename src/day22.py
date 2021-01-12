import math
import re
from collections import deque
from dataclasses import dataclass
from typing import List

import toolz


def read_input() -> List[str]:
    with open("../input/day22.txt") as f:
        return f.readlines()


@dataclass
class Node:
    x: int
    y: int
    size: int
    used: int
    avail: int
    use: int


def parse_input(lines: List[str], offset: int = 2) -> List[Node]:
    return [
        Node(
            x=int(match.group(1)),
            y=int(match.group(2)),
            size=int(match.group(3)),
            used=int(match.group(4)),
            avail=int(match.group(5)),
            use=int(match.group(6)),
        )
        for line in lines[offset:]
        if (match := re.match(r"/dev/grid/node-x(\d+)-y(\d+)\s+(\d+)T\s*(\d+)T\s*(\d+)T\s*(\d+)%", line)) is not None
    ]


def count_viable_pairs(nodes: List[Node]) -> int:
    count = 0
    for i, n1 in enumerate(nodes):
        if n1.used > 0:
            for j, n2 in enumerate(nodes):
                if n1.used <= n2.avail and i != j:
                    count += 1

    return count

def bfs(nodes: List[Node]) -> int:
    max_x = max(n.x for n in nodes) + 1
    max_y = max(n.y for n in nodes) + 1
    sorted_nodes = sorted(nodes, key=lambda n: (n.y, n.x))
    zero_node = toolz.first(n for n in nodes if n.used == 0)
    grid = tuple(
        "#" if n.used > zero_node.avail
        else "G" if n.x == max_x - 1 and n.y == 0
        else "_" if n.x == zero_node.x and n.y == zero_node.y
        else "."
        for n in sorted_nodes
    )
    print("\n".join("".join(line) for line in toolz.partition(max_x, grid)))
    initial_state = (grid, zero_node.x, zero_node.y)
    states = {initial_state}
    q = deque()
    q.append((initial_state, 0))

    while q:
        (grid, zero_x, zero_y), steps = q.popleft()

        possible_moves = [
            (new_x, new_y)
            for xd, yd in [(0, -1), (-1, 0), (0, 1), (1, 0), ]
            if 0 <= (new_x := zero_x + xd) < max_x
            if 0 <= (new_y := zero_y + yd) < max_y
            if grid[new_y * max_x + new_x] in {".", "G"}
        ]

        for (target_x, target_y) in possible_moves:
            new_grid = list(grid)

            new_grid[target_y * max_x + target_x], new_grid[zero_y * max_x + zero_x] = \
                new_grid[zero_y * max_x + zero_x], new_grid[target_y * max_x + target_x]

            if new_grid[0] == "G":
                return steps + 1
            else:
                new_state = (tuple(new_grid), target_x, target_y)
                if new_state not in states:
                    states.add(new_state)
                    q.append((new_state, steps + 1))

    return -1


def test_part1():
    print(count_viable_pairs(parse_input(read_input())))


def test_part2_example():
    example = """Filesystem            Size  Used  Avail  Use%
/dev/grid/node-x0-y0   10T    8T     2T   80%
/dev/grid/node-x0-y1   11T    6T     5T   54%
/dev/grid/node-x0-y2   32T   28T     4T   87%
/dev/grid/node-x1-y0    9T    7T     2T   77%
/dev/grid/node-x1-y1    8T    0T     8T    0%
/dev/grid/node-x1-y2   11T    7T     4T   63%
/dev/grid/node-x2-y0   10T    6T     4T   60%
/dev/grid/node-x2-y1    9T    8T     1T   88%
/dev/grid/node-x2-y2    9T    6T     3T   66%"""
    nodes = parse_input(example.splitlines(), offset=1)
    assert bfs(nodes) == 7


def test_part2():
    print(bfs(parse_input(read_input())))

