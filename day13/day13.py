import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math


def part1(start, buses):
    time  = 1000000000
    bus   = 0
    delay = 0
    for b in buses:
        if b != 'x':
            t = int(b)
            d = (int(start / t) + 1) * t
            if d < time:
                time  = d
                bus   = t
                delay = d - start
    return bus * delay


def combine(offset, repeat, bus, index):
    off = 0
    rep = 0    
    t   = offset

    while True:
        if (t + index) % bus == 0:
            off = t
            break
        t += repeat

    t += repeat
    while True:
        if (t + index) % bus == 0:
            rep = t - off
            break
        t += repeat

    return [off, rep]   


def part2(buses):
    times = []   
    for i in range(len(buses)):
        if buses[i] != 'x':
            times.append([i, int(buses[i])])

    offset = times[0][0]
    repeat = times[0][1]

    for time in times[1:]:
        result = combine(offset, repeat, time[1], time[0])
        offset = result[0]
        repeat = result[1]

    return offset  


def solution(file):
    print("Input: ", file)

    lines = ut.read_lines(file)
    start = int(lines[0])
    buses = lines[1].split(',')

    p1 = part1(start, buses)
    print("Part1: ", p1)

    p2 = part2(buses)
    print("Part2: ", p2)


def main():
    # 17,x,13,19 is 3417.
    # 67,7,59,61 first occurs at timestamp 754018.
    # 67,x,7,59,61 first occurs at timestamp 779210.
    # 67,7,x,59,61 first occurs at timestamp 1261476.
    # 1789,37,47,1889 first occurs at timestamp 1202161486.
    # part2('17,x,13,19'.split(','))
    # part2('67,7,59,61'.split(','))
    # part2('67,x,7,59,61'.split(','))
    # part2('67,7,x,59,61'.split(','))
    # part2('1789,37,47,1889'.split(','))

    solution("day13-test.txt");
    solution("day13-input.txt");

if __name__ == '__main__':
    main()

