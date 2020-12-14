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


# Using Chinese Remainder Theorem
def part2_crt(buses):
    # (x + times[0]) % times[1] == 0 for all buses. Find x.
    times   = []   
    # Product of all the bus periods - these are primes, so coprime.
    product = 1
    for i in range(len(buses)):
        if buses[i] != 'x':
            product *= int(buses[i])
            times.append([i, int(buses[i])])

    total = 0
    for time in times:
        factor = 0
        # term % time[i] == 0 for all but the current bus 
        term   = (product // time[1])
        # Inverse mod operation
        while ((term * factor + time[0]) % time[1]) != 0:
            factor += 1
        total = total + term * factor 

    #print(times, total % product)
    return total % product  


# Simpler version of my original code - amazing what relaxing to think can do.
# Actually, this is apparently a sieve search. Does the job anyway, and is the 
# simplest to understand.
def part2_again(buses):
    times = []   
    for i in range(len(buses)):
        if buses[i] != 'x':
            times.append([i, int(buses[i])])

    offset = 0
    period = times[0][1]
    for i in range(1, len(times)):
        t = times[i]
        while (offset + t[0]) % t[1] != 0:
            offset += period
        period *= t[1] 

    print(times, offset)
    return offset  


def solution(file):
    print("Input: ", file)

    lines = ut.read_lines(file)
    start = int(lines[0])
    buses = lines[1].split(',')

    p1 = part1(start, buses)
    print("Part1: ", p1)

    #p2 = part2(buses)
    #p2 = part2_crt(buses)
    p2 = part2_again(buses)
    print("Part2: ", p2)


def main():
    # 17,x,13,19 is 3417.
    # 67,7,59,61 first occurs at timestamp 754018.
    # 67,x,7,59,61 first occurs at timestamp 779210.
    # 67,7,x,59,61 first occurs at timestamp 1261476.
    # 1789,37,47,1889 first occurs at timestamp 1202161486.
    # part2_crt('17,x,13,19'.split(','))
    # part2_crt('67,7,59,61'.split(','))
    # part2_crt('67,x,7,59,61'.split(','))
    # part2_crt('67,7,x,59,61'.split(','))
    # part2_crt('1789,37,47,1889'.split(','))

    part2_again('17,x,13,19'.split(','))
    part2_again('67,7,59,61'.split(','))
    part2_again('67,x,7,59,61'.split(','))
    part2_again('67,7,x,59,61'.split(','))
    part2_again('1789,37,47,1889'.split(','))

    solution("day13-test.txt")
    solution("day13-input.txt")


if __name__ == '__main__':
    main()

