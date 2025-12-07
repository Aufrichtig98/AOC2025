import aoc_helper
from collections import defaultdict
from functools import *
from itertools import *

def part_one():
    requests = list()
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(line.strip("\n").split(" "))

    mathe_problems = list()
    for line in requests[:-1]:
        current_line = list()
        for element in line:
            if element != "":
                current_line.append(int(element))
        mathe_problems.append(current_line)
    current_line = list()
    for element in requests[-1]:
        if element != "":
            current_line.append(element)
    mathe_problems.append(current_line)

    mathe_problems = list(zip(*mathe_problems))
    result = 0
    for problem in mathe_problems:
        operator = problem[-1]
        if operator == "*":
            tmp = 1
        else:
            tmp = 0
        for value in problem[:-1]:
            if operator == "*":
                tmp *= value
            else:
                tmp += value
        result += tmp
    print(result)


if __name__ == '__main__':
    requests = list()
    max_len = 0
    with open("input.txt", "rt") as myfile:
        for line in myfile:
            requests.append(list(line.strip("\n")))
            max_len = max(max_len, len(requests[-1]))
    for i in range(len(requests)):
        if len(requests[i]) != max_len:
            requests[i] = requests[i] + [' '] * (max_len - len(requests[i]))
    mathe_problems = list(zip(*requests[:-1]))
    mathe_problems = list(map(lambda x: list(x), mathe_problems))
    operator = list(reduce(lambda x,y: x + y if y != ' ' else x, requests[-1]))
    tmp = list()
    mathe_problems_reduced = list()
    for i in range(len(mathe_problems)):
        if reduce(lambda x,y: x+y, mathe_problems[i]).strip(' ') != '':
            tmp.append(mathe_problems[i])
        else:
            mathe_problems_reduced.append(tmp)
            tmp = list()
    mathe_problems_reduced.append(tmp)
    mathe_problems = mathe_problems_reduced
    tmp = list()
    mathe_problems_tranposed = list()
    for problem in mathe_problems:
        for value in problem:
            tmp.append(int(reduce(lambda x,y: x + y if y != ' ' else x, value)))
        mathe_problems_tranposed.append(tmp)
        tmp = list()
    mathe_problems = mathe_problems_tranposed
    for i in range(len(mathe_problems)):
        mathe_problems[i].append(operator[i])
    result = 0
    for problem in mathe_problems:
        operator = problem[-1]
        if operator == "*":
            tmp = 1
        else:
            tmp = 0
        for value in problem[:-1]:
            if operator == "*":
                tmp *= value
            else:
                tmp += value
        result += tmp
    print(result)