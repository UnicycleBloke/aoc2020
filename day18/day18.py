import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut
from copy import deepcopy
import math
from functools import reduce

def evaluate(expr):
    items = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    output = []
    stack  = []

    for c in items:
        if c == '+': 
            while len(stack) > 0 and stack[-1] != '(':
                op = stack.pop()
                output.append(op)
            stack.append(c)
        elif c == '*':
            while len(stack) > 0 and stack[-1] != '(':
                op = stack.pop()
                output.append(op)
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) > 0 and stack[-1] != '(':
                op = stack.pop()
                output.append(op)
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
        else:
            output.append(int(c))

    for i in range(len(stack)):
        op = stack.pop()
        output.append(op)

    stack2 = []
    for c in output:
        if c == '+': 
            a = stack2.pop()
            b = stack2.pop()
            stack2.append(a + b)
        elif c == '*':
            a = stack2.pop()
            b = stack2.pop()
            stack2.append(a * b)
        else:
            stack2.append(c)

    return stack2[0]


def evaluate2(expr):
    items = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    output = []
    stack  = []

    for c in items:
        if c == '+': 
            while (len(stack) > 0) and (stack[-1] != '(') and (stack[-1] != '*'):
                op = stack.pop()
                output.append(op)
            stack.append(c)
        elif c == '*':
            while (len(stack) > 0) and (stack[-1] == '+'): 
                op = stack.pop()
                output.append(op)
            stack.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) > 0 and stack[-1] != '(':
                op = stack.pop()
                output.append(op)
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
        else:
            output.append(int(c))

    for i in range(len(stack)):
        op = stack.pop()
        output.append(op)

    stack2 = []
    for c in output:
        if c == '+': 
            a = stack2.pop()
            b = stack2.pop()
            stack2.append(a + b)
        elif c == '*':
            a = stack2.pop()
            b = stack2.pop()
            stack2.append(a * b)
        else:
            stack2.append(c)

    return stack2[0]


def part1(data):
    total = 0
    for expr in data:
        total = total + evaluate(expr)
    return total


def part2(data):
    total = 0
    for expr in data:
        total = total + evaluate2(expr)
    return total


def solution(file):
    print("Input: ", file)
    lines = ut.read_lines(file)

    data = lines

    p1 = part1(data)
    print("Part1: ", p1)
    p2 = part2(data)
    print("Part2: ", p2)


def main():
    solution("day18-test.txt")
    solution("day18-input.txt")


if __name__ == '__main__':
    main()

