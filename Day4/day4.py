from aoc_helper import get_elments_directions, DIRECTION_WITH_DIAG
from collections import defaultdict
from functools import *
from itertools import *

def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))

    result = 0
    for i in range(len(requests)):
        for j in range(len(requests[i])):
            if requests[i][j] == ".":
                continue
            valid_dir = get_elments_directions(1, requests, (i,j), DIRECTION_WITH_DIAG)
            seen_paper = 0
            for pos_x, pos_y in valid_dir:
                if requests[pos_x][pos_y] == "@":
                    seen_paper += 1
            if seen_paper < 4:
                result += 1
    print(result)

if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))

    result = 0
    i = 0
    j = 0
    repeat = False
    removed = 0
    while (not repeat) :
        repeat = True
        for i in range(len(requests)):
            for j in range(len(requests[i])):
                if requests[i][j] == ".":
                    continue
                valid_dir = get_elments_directions(1, requests, (i,j), DIRECTION_WITH_DIAG)
                seen_paper = 0
                for pos_x, pos_y in valid_dir:
                    if requests[pos_x][pos_y] == "@":
                        seen_paper += 1
                if seen_paper < 4:
                    requests[i][j] = "."
                    removed += 1
                    repeat = False
    print (removed)
