import dataclasses
from collections import deque
from dataclasses import dataclass
from enum import Enum
from functools import cached_property
from itertools import combinations, product
from typing import Tuple, List, Iterator


class ItemType(Enum):
    Microchip = ("microchip",)
    Generator = "generator"


@dataclass(frozen=True)
class Item(object):
    material: str
    type: ItemType


@dataclass(frozen=True)
class BoardState(object):
    elevator_floor: int
    item_floors: Tuple[int, ...]

    @cached_property
    def score(self) -> int:
        return sum(self.item_floors)


def iter_next_states(state: BoardState) -> Iterator[BoardState]:
    next_floors = []
    if state.elevator_floor < 4:
        next_floors.append(state.elevator_floor + 1)
    if state.elevator_floor > 1:
        next_floors.append(state.elevator_floor - 1)

    floor_items = [i for i in range(len(state.item_floors)) if state.item_floors[i] == state.elevator_floor]

    item_selection = []
    for item in floor_items:
        item_selection.append([item])
    for items in combinations(floor_items, 2):
        item_selection.append(items)

    for next_floor, items in product(next_floors, item_selection):
        next_items = tuple(next_floor if i in items else state.item_floors[i] for i in range(len(state.item_floors)))
        yield BoardState(elevator_floor=next_floor, item_floors=next_items)


def is_legal_state(items: List[Item], state: BoardState) -> bool:
    return all(is_legal_floor(items, state, floor) for floor in range(1, 5))


def is_legal_floor(items: List[Item], state: BoardState, floor: int):
    generators = [
        items[i]
        for i in range(len(state.item_floors))
        if state.item_floors[i] == floor and items[i].type == ItemType.Generator
    ]
    if generators:
        microchips = [
            items[i]
            for i in range(len(state.item_floors))
            if state.item_floors[i] == floor and items[i].type == ItemType.Microchip
        ]
        res = all(dataclasses.replace(chip, type=ItemType.Generator) in generators for chip in microchips)
        return res
    else:
        return True


def bfs(items: List[Item], initial_state: BoardState) -> int:
    q = deque()
    final_state = BoardState(elevator_floor=4, item_floors=(4,) * len(items))
    seen = {initial_state}
    q.append((0, initial_state))

    while q:
        (steps, state) = q.popleft()
        next_steps = steps + 1
        for next_state in iter_next_states(state):
            if next_state == final_state:
                return next_steps
            elif next_state not in seen and is_legal_state(items, next_state):
                seen.add(next_state)
                q.append((next_steps, next_state))

    return -1


def test_part1_example():
    items = [
        Item("H", ItemType.Generator),
        Item("H", ItemType.Microchip),
        Item("L", ItemType.Generator),
        Item("L", ItemType.Microchip),
    ]
    initial_state = BoardState(1, (2, 1, 3, 1))
    res = bfs(items, initial_state)
    assert res == 11


def test_part1():
    items = [
        Item("polonium", ItemType.Generator),
        Item("polonium", ItemType.Microchip),
        Item("thulium", ItemType.Generator),
        Item("thulium", ItemType.Microchip),
        Item("promethium", ItemType.Generator),
        Item("promethium", ItemType.Microchip),
        Item("ruthenium", ItemType.Generator),
        Item("ruthenium", ItemType.Microchip),
        Item("cobalt", ItemType.Generator),
        Item("cobalt", ItemType.Microchip),
    ]
    initial_state = BoardState(1, (1, 2, 1, 1, 1, 2, 1, 1, 1, 1))
    res = bfs(items, initial_state)
    print(res)
    assert res == 47


def test_part2():
    items = [
        Item("cobalt", ItemType.Generator),
        Item("cobalt", ItemType.Microchip),
        Item("elerium", ItemType.Generator),
        Item("elerium", ItemType.Microchip),
        Item("dilithium", ItemType.Generator),
        Item("dilithium", ItemType.Microchip),
    ]
    initial_state = BoardState(4, (4, 4, 1, 1, 1, 1))
    res = bfs(items, initial_state) + 47
    assert res == 71
