import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *


def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n")
            if tmp[0] == 'L':
                requests.append(-int(tmp[1:]))
            else:
                requests.append(int(tmp[1:]))

    numer_of_zero = 0
    current_values = 50
    for rotation in requests:
        current_values += rotation
        current_values %= 100
        if current_values == 0:
            numer_of_zero += 1


if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n")
            if tmp[0] == 'L':
                requests.append(-int(tmp[1:]))
            else:
                requests.append(int(tmp[1:]))

    numer_of_zero = 0
    current_values = 50
    before_rotation = current_values
    for rotation in requests:
        numer_of_zero += (abs(rotation) // 100)
        if rotation < 0:
            rotation = (abs(rotation) % 100) * -1
        else:
            rotation %= 100
        before_rotation = current_values
        current_values += rotation
        current_values %= 100
        if (((rotation > 0 and current_values < before_rotation) or (
                rotation < 0 and current_values > before_rotation)) and before_rotation != 0) or current_values == 0:
            numer_of_zero += 1

    print(numer_of_zero)
