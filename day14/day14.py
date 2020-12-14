import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math


def part1(data):
    memory   = {}
    and_mask = 0
    or_mask  = 0

    for d in data:
        s   = d.split()
        key = s[0][0:3]

        if key == 'mem':
            addr  = int(s[0][4:-1])
            value = int(s[2])
            memory[addr] = (value & ~and_mask) | or_mask

        if key == 'mas':
           and_mask = int(deepcopy(s[2]).replace('1', 'X').replace('0', '1').replace('X', '0'), 2)
           or_mask  = int(deepcopy(s[2]).replace('X', '0'), 2)

    return sum([memory[x] for x in memory])


def addresses(addr, mask):
    res = [addr]

    for b in range(len(mask)):
        c = mask[len(mask) - b - 1]
        if c == '1':
            r = len(res)
            for i in range(r):
                res[i] = res[i] | (1 << b)
        if c == 'X':
            r = len(res)
            for i in range(r):                
                res.append(res[i] | (1 << b))
                res[i] = (res[i] & ~(1 << b))

    return res


def part2(data):
    memory = {}
    mask   = ''  

    for d in data:
        s   = d.split()
        key = s[0][0:3]

        if key == 'mem':
            base  = int(s[0][4:-1])
            value = int(s[2])

            addrs = addresses(base, mask)
            for addr in addrs:
                memory[addr] = value

        if key == 'mas':
           mask = s[2]

    return sum([memory[x] for x in memory])


def solution(file, do1, do2):
    print("Input: ", file)
    data = ut.read_lines(file)

    if do1:
        p1 = part1(data)
        print("Part1: ", p1)

    if do2:
        p2 = part2(data)
        print("Part2: ", p2)


def main():
    primes = ut.read_primes()

    # Bodge here to run with different files for parts 1 and 2.
    solution("day14-test-p1.txt", True,  False)
    solution("day14-test-p2.txt", False, True)
    solution("day14-input.txt",   True,  True)


if __name__ == '__main__':
    main()

