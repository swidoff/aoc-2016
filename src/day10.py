from typing import List, Dict
import networkx as nx
import re

from toolz.tests.test_dicttoolz import defaultdict


def read_input() -> List[str]:
    with open("../input/day10.txt") as f:
        return f.readlines()


def parse_input(lines: List[str]) -> (nx.DiGraph, Dict[str, List[int]]):
    graph = nx.DiGraph()
    values = defaultdict(list)

    for line in lines:
        if match := re.match(r"value (\d+) goes to (bot \d+)", line):
            value = int(match.group(1))
            node = match.group(2)
            graph.add_node(node)
            values[node].append(value)
        elif match := re.match(r"(bot \d+) gives low to (\w+ \d+) and high to (\w+ \d+)", line):
            src_bot = match.group(1)
            lo_bot = match.group(2)
            hi_bot = match.group(3)
            graph.add_node(src_bot)
            graph.add_node(lo_bot)
            graph.add_node(hi_bot)
            graph.add_edge(src_bot, lo_bot, func=min)
            graph.add_edge(src_bot, hi_bot, func=max)

    return graph, values


def part1(graph: nx.DiGraph, values: Dict[str, List[int]]) -> str:
    sorted_nodes = nx.topological_sort(graph)
    for node in sorted_nodes:
        node_values = values[node]
        if 61 in node_values and 17 in node_values:
            return node

        for (_, out_node, func) in graph.out_edges(nbunch=node, data="func"):
            values[out_node].append(func(node_values))

    return ""


def part2(graph: nx.DiGraph, values: Dict[str, List[int]]) -> str:
    sorted_nodes = nx.topological_sort(graph)
    for node in sorted_nodes:
        node_values = values[node]

        for (_, out_node, func) in graph.out_edges(nbunch=node, data="func"):
            values[out_node].append(func(node_values))

    return ""


def test_part1():
    graph, values = parse_input(read_input())
    print(part1(graph, values))


def test_part2():
    graph, values = parse_input(read_input())
    part2(graph, values)
    print(values["output 0"], values["output 1"], values["output 2"])
    print(values["output 0"][0] * values["output 1"][0] * values["output 2"][0])
