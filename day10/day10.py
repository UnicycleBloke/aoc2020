import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def part1(data):
    j1 = 0
    j3 = 0
    base = 0
    for i in range(len(data)):
        j = min([x for x in data if base < x <= (base + 3)])
        if (j - base) == 1:
            j1 += 1
        if (j - base) == 3:
            j3 += 1
        base = j

    return j1 * (j3 + 1)    


def ways(data, base, index, info):
    if base == max(data):
        return 1

    key = base * 10000 + index
    if key in info:
        return info[key]   

    w = 0
    ads = [x for x in data if base < x <= (base + 3)]
    for a in ads:
        if a in data:
            w = w + ways(data, a, index + 1, info)

    info[key] = w   
    return w    


def part2(data): 
    info = {}
    return ways(data, 0, 0, info)


def solution(file):
    print("Input: ", file)

    lines = ut.read_lines(file)
    nums = [int(x) for x in lines]

    p1 = part1(nums)
    print("Part1: ", p1)

    p2 = part2(nums)
    print("Part2: ", p2)


def main():
    solution("day10-test.txt");
    solution("day10-test2.txt");
    solution("day10-input.txt");


if __name__ == '__main__':
    main()

