import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def contains(value, pre):
    for i in range(len(pre)):
        for j in range(i, len(pre)):
            if pre[i] + pre[j] == value:
                return True
    
    return False


def part1(nums, size):
    print('Part1:')
    pre = nums[0:size]
    for i in range(size, len(nums)):
        if not contains(nums[i], pre):
            print(nums[i])
            return nums[i]
        pre = pre[1:] + [nums[i]]


def part2(nums, value):     
    print('Part2:')
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            tot = nums[i:j]
            if sum(tot) == value:
                print(min(tot) + max(tot))
                return
            if sum(tot) > value:
                break


def main():
    if len(sys.argv) < 2:
        print('Provide input file name')
        exit(-1)
    if len(sys.argv) < 3:
        print('Provide preamble length')
        exit(-1)

    lines = ut.read_lines(sys.argv[1])
    nums = [int(x) for x in lines]

    value = part1(nums, int(sys.argv[2]))
    part2(nums, value)   


if __name__ == '__main__':
    main()
