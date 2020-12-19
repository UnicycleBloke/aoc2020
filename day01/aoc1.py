import sys


def part1(data):
    print('Part 1')
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            di = data[i]
            dj = data[j]
            if (di + dj == 2020):
                print('    ', di, dj, di * dj)


def part2(data):
    print('Part 2')
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            for k in range(j + 1, len(data)):
                di = data[i]
                dj = data[j]
                dk = data[k]
                if (di + dj + dk == 2020):
                    print('    ', di, dj, dk, di * dj * dk)


def solution(filename):
    print('Input file : {}'.format(filename))
    file = open(filename)
    lines = file.readlines()

    data = [int(line.strip()) for line in lines]

    part1(data)
    print()            

    part2(data)
    print()            


def main():
    print('AOC problem #1')
    if len(sys.argv) < 2:
        print('Supply at least one input file name')
        exit(1)

    for filename in sys.argv[1:]:
        solution(filename)
    

if __name__ == '__main__':
    # Execute only if run as a script
    main()
