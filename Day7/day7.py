import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *

import debug_helper


def part_one():
    grid = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            grid.append(list(line.strip("\n")))
    start_column = 0
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            start_column = i
            break
    grid_depth = len(grid)
    beams = [(0, start_column)]
    split = 0
    while beams:
        current_beam = beams.pop()
        break_out = False
        while(current_beam[0] != grid_depth - 1 and grid[current_beam[0]][current_beam[1]] != "^"):
            if grid[current_beam[0]][current_beam[1]] == "#":
                break_out = True
                break
            grid[current_beam[0]][current_beam[1]] = "#"
            current_beam = aoc_helper.add_tuple(current_beam, (1,0))
        if current_beam[0] == grid_depth - 1 or break_out:
            grid[current_beam[0]][current_beam[1]] = "#"
            continue
        else:
            split += 1
            beams.append(aoc_helper.add_tuple(current_beam, (0,1)))
            beams.append(aoc_helper.add_tuple(current_beam, (0,-1)))
    print_map(grid)
    print(split)

def print_map(map):
    print("\n")
    for i in map:
        print(i)
def part_two():
    grid = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            grid.append(list(line.strip("\n")))
    start_column = 0
    for i in range(len(grid[0])):
        if grid[0][i] == "S":
            start_column = i
            break
    for i in range(len(grid)):
        grid[i] = list(map(lambda x: "0" if x == "." else "^", grid[i]))
    grid[0][start_column] = "0"

    beam_count = defaultdict(int)

    beam_count[start_column] += 1
    splitters = list()
    for row in grid:
        splitters.append({column for column, value in enumerate(row) if value == "^"})

    for splitter in splitters:
        for activel_splitter in (splitter & set(beam_count)):
            beam_count[activel_splitter + 1] += beam_count[activel_splitter]
            beam_count[activel_splitter - 1] += beam_count[activel_splitter]
            beam_count[activel_splitter] = 0

    print(sum(beam_count.values()))

part_two()
