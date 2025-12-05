import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *

def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(aoc_helper.list_of_intstr_to_int(list(line.strip("\n"))))

    result = 0

    for battery_pack in requests:
        left_index = 0
        highest_l_value = 0
        for idx, value in enumerate(battery_pack[:-1]):
            if value > highest_l_value:
                highest_l_value = value
                left_index = idx

        highest_r_value = 0
        for i in range(left_index + 1, len(battery_pack)):
            if battery_pack[i] > highest_r_value:
                highest_r_value = battery_pack[i]

        result += highest_l_value * 10 + highest_r_value

    print(result)

if __name__ == '__main__':
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(aoc_helper.list_of_intstr_to_int(list(line.strip("\n"))))

    result = 0


    for battery_pack in requests:
        result_current_battery = list()
        numbers_left = 12
        left_index = -1
        highest_l_value = 1
        while numbers_left:
            left_index += 1
            for idx in range(left_index,  len(battery_pack) - (numbers_left-1)):
                if battery_pack[idx] > highest_l_value:
                    highest_l_value = battery_pack[idx]
                    left_index = idx
            result_current_battery.append(str(highest_l_value))
            numbers_left -= 1
            highest_l_value = 1
        result += int(reduce(lambda x,y: x + y, result_current_battery))

    print(result)