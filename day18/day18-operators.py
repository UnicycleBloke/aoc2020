import sys
import os
import re
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


# Alternative solution which fudges the operator precedence 
# with overloading and substitution.
def part1(data):
    class Int:
        def __init__(self, value):
            self.value = value
        def __add__(self, other): # Meaning unchanged
            result = self.value + other.value 
            return Int(result)
        def __sub__(self, other): # prec(-) == prec(+) so use this to perform *
            result = self.value * other.value 
            return Int(result)

    total = 0
    for expr in data:
        total += eval(re.sub('([0-9]+)', r'Int(\1)', expr).replace('*', '-')).value
    return total


def part2(data):
    class Int:
        def __init__(self, value):
            self.value = value
        def __mul__(self, other): # prec(*) > prec(+) so use this to perform +
            result = self.value + other.value 
            return Int(result)
        def __sub__(self, other): # prec(-) < prec(*) so use this to perform *
            result = self.value * other.value 
            return Int(result)

    total = 0
    for expr in data:
        total += eval(re.sub('([0-9]+)', r'Int(\1)', expr).replace('*', '-').replace('+', '*')).value
    return total


def solution(file):
    print("Input: ", file)
    data = ut.read_lines(file)
    print("Part1: ", part1(data))
    print("Part2: ", part2(data))


def main():
    #solution("day18-test.txt")
    solution("day18-input.txt")


if __name__ == '__main__':
    main()

