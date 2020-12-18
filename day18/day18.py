import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


def convert_to_rpn1(expr):
    items = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    output = []
    stack  = []

    for c in items:
        if c in ['+', '*']: 
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
    
    return output


def convert_to_rpn2(expr):
    items = expr.replace('(', ' ( ').replace(')', ' ) ').split()
    output = []
    stack  = []

    for c in items:
        if c in ['+', '*']: 
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
    
    return output


def evaluate(rpn):
    stack = []
    for c in rpn:
        if c == '+': 
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        elif c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        else:
            stack.append(c)
    return stack[0]


def part1(data):
    total = 0
    for expr in data:
        rpn = convert_to_rpn1(expr)
        total = total + evaluate(rpn)
    return total


def part2(data):
    total = 0
    for expr in data:
        rpn = convert_to_rpn2(expr)
        total = total + evaluate(rpn)
    return total


def solution(file):
    print("Input: ", file)
    data = ut.read_lines(file)

    p1 = part1(data)
    print("Part1: ", p1)

    p2 = part2(data)
    print("Part2: ", p2)


def main():
    solution("day18-test.txt")
    solution("day18-input.txt")


if __name__ == '__main__':
    main()

