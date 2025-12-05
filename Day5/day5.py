import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *

def part_one():
    ids = list()
    ranges = list()
    switch = False
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            if line == "\n":
                switch = True
                continue
            if switch:
                ids.append(int(line.strip("\n")))
            else:
                ranges.append(tuple(aoc_helper.list_of_intstr_to_int(line.strip("\n").split("-"))))
    sorted(ranges)

    result = 0

    for ingredient in ids:
        for range in ranges:
            if range[0] <= ingredient <= range[1]:
                result += 1
                break
    print(result)


if __name__ == '__main__':
    ids = list()
    ranges = list()
    switch = False
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            if line == "\n":
                switch = True
                continue
            if switch:
                ids.append(int(line.strip("\n")))
            else:
                ranges.append(tuple(aoc_helper.list_of_intstr_to_int(line.strip("\n").split("-"))))
    ranges = sorted(ranges)

    result = 0
    idx = 0

    while idx < len(ranges)-1:
        if ranges[idx][1] >= ranges[idx+1][0]:
            ranges[idx] = min(ranges[idx][0], ranges[idx + 1][0]),max(ranges[idx][1],ranges[idx + 1][1])
            ranges.remove(ranges[idx+1])
        else:
            idx += 1

    for interval in ranges:
        result += (interval[1] - interval[0] + 1)

    print(result)