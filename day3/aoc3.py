lines = open('aoc3-input.txt').readlines()

grid = []
for line in lines:
    grid.append([c for c in line.strip()])

def count_trees(c, r):
    row   = 0
    col   = 0
    trees = 0

    while row < len(grid): 
        if (grid[row][col] == '#'):
            trees = trees + 1
        row   = row + r
        col   = (col + c) % len(grid[0])

    return trees    

t1  = count_trees(1, 1)
t2  = count_trees(3, 1)
t3  = count_trees(5, 1)
t4  = count_trees(7, 1)
t5  = count_trees(1, 2)

print(t1, t2, t3, t4, t5, t1*t2*t3*t4*t5)


