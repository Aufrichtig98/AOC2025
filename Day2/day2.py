import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *

def built_all_sequenccs(sequence, length):
    result = list()
    while sequence:
        result.append(sequence[:length])
        sequence = sequence[length:]
    return result

def check_illegal_part_one(id):
    id = str(id)
    if len(id) % 2:

        left_part = id[:-(len(id)//2)]
        right_part = id[(len(id)//2):]
    return left_part == right_part

def check_illegal_part_two(id):
    id = str(id)
    for i in range(1, len(id)//2 + 1):
        if len(id) % i != 0:
            continue
        else:
            all_sequences = built_all_sequenccs(id, i)
            if len(set(all_sequences)) == 1:
                return True

    return False


def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n").split(",")
            for request in tmp:
                requests.append(aoc_helper.list_of_intstr_to_int(request.split("-")))

    result = 0
    for request in requests:
        for i in range(request[0], request[1]+1):
            if check_illegal_part_one(i):
                result += i

    print(result)

if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            tmp = line.strip("\n").split(",")
            for request in tmp:
                requests.append(aoc_helper.list_of_intstr_to_int(request.split("-")))

    result = 0
    for request in requests:
        for i in range(request[0], request[1]+1):
            if check_illegal_part_two(i):
                result += i

    print(result)