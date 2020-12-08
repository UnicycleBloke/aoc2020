import re
import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut

def run(prog, part1):
    acc = 0
    pc  = 0
    while True:
        if pc == len(prog):
            print('OK:', acc)
            return True

        inst = prog[pc]

        if inst[2]:
            if part1:
                # Reduce clutter for part 2 
                print('ERROR:', acc)
            return False

        inst[2] = True    
        if inst[0] == 'acc':
            acc += inst[1]
            pc  += 1
        elif inst[0] == 'nop':     
            pc  += 1
        elif inst[0] == 'jmp':     
            pc  += inst[1]


def part1(prog):
    print('Part1:')
    run(prog, True)


def part2(prog):
    print('Part2:')
    for i in range(len(prog)):
        prog2 = [p[:] for p in prog]

        if prog2[i][0] == 'nop':
            prog2[i][0] = 'jmp'
            if run(prog2, False):
                return

        elif prog2[i][0] == 'jmp':
            prog2[i][0] = 'nop'
            if run(prog2, False):
                return

def main():
    if len(sys.argv) < 2:
        print('Provide input file name')
        exit(-1)

    lines = ut.read_lines(sys.argv[1])
    prog  = []
    for line in lines:
        m = re.match('^(\w+)\s+(.)(\d+)$', line)
        sign = 1 if m.group(2) == '+' else -1
        inst = [m.group(1), sign * int(m.group(3)), False]
        prog.append(inst)

    # Deep copy prog because Python
    part1([p[:] for p in prog])
    #part2([p[:] for p in prog])    


if __name__ == '__main__':
    main()
