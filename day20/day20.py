import sys
import os
import math
sys.path.insert(1, os.path.join(sys.path[0], '..'))
import utils.utils as ut


class Tile:
    def __init__(self):
        self.id    = 0
        self.bits  = ['0'] * 100
        self.types = []

    def top(self):
        return ''.join(self.bits[0:10])
    def bottom(self):
        return ''.join(self.bits[90:100])
    def left(self):
        return ''.join(x for x in [self.bits[10*r] for r in range(10)])
    def right(self):
        return ''.join(x for x in [self.bits[10*r+9] for r in range(10)])

    def edge_values(self):
        top    = int(self.top(), 2)
        bottom = int(self.bottom(), 2)
        left   = int(self.left(), 2)
        right  = int(self.right(), 2)
        return [top, right, bottom, left]

    def all_edge_values(self):
        result = set(self.edge_values())
        self.flip_horz()    
        result = result.union(set(self.edge_values()))
        self.flip_horz()    
        self.flip_vert()    
        result = result.union(set(self.edge_values()))
        self.flip_vert() 
        return result   

    def doflip(self):
        self.flip_horz()

    def flip_horz(self):
        bits = ['0'] * 100
        for r in range(10):
            for c in range(10):
                bits[10*r+c] = self.bits[10*r + 10-c-1]
        self.bits = bits

    def flip_vert(self):
        bits = ['0'] * 100
        for r in range(10):
            for c in range(10):
                bits[10*r+c] = self.bits[10*(10-r-1) + c]
        self.bits = bits

    def rotate(self):
        bits = ['0'] * 100
        for r in range(10):
            for c in range(10):
                bits[10*r + c] = self.bits[10*c + 10-r-1]
        self.bits = bits

    def print(self):
        print(self.id, self.edges())
        for r in range(10):
            print(self.bits[10*r:10*(r+1)])
        print()    


def tile_fits_below(prev, curr):
    bottom = prev.bottom()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    curr.rotate()
    curr.doflip()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    curr.rotate()
    if bottom == curr.top(): return True
    return False


def tile_fits_right(prev, curr):
    right = prev.right()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    curr.rotate()
    curr.doflip()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    curr.rotate()
    if right == curr.left(): return True
    return False


def find_monsters2(image, kernel):
    # All the # in the image
    total = sum(sum(i) for i in image)
    # All the # in the monster
    need  = sum(sum(k) for k in kernel)
    found = 0
    for x in range(len(image) - len(kernel)):
        for y in range(len(image[0]) - len(kernel[0])):
            # Is there a monster at (x, y)?
            count = sum([1 for i in range(len(kernel)) for j in range(len(kernel[0])) if image[x+i][y+j] == 1 and kernel[i][j] == 1])
            if count == need:
                found += 1 
                # Let's hope monsters don't overlap.
                total -= need
    
    if found > 0:
        #print('Monsters={} Roughness={}'.format(found, total))
        print('Part2: ', total)
        exit(0)


def find_monsters(grid):
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '  
    ]    
    nessie = [[1 if c == '#' else 0 for c in m] for m in monster]

    dim  = len(grid)
    size = 8 * dim
    image = [[8 for i in range(size)] for j in range(size)]
    for r in range(dim):
        for c in range(dim):
            t = grid[r][c]
            for i in range(8):
                for j in range(8):
                    v = int(t.bits[10*(i+1)+(j+1)])
                    image[r*8+i][c*8+j] = v
    
    find_monsters2(image, nessie)


# Recursively check for the edges matching correctly.
def assemble_image3(tiles, grid, used, size):
    if len(tiles)== len(used):
        find_monsters(grid)

    n = len(used)
    col = n % size
    row = n // size 

    check_left  = True if col > 0 else False
    check_above = True if row > 0 else False

    for curr in tiles:
        if curr in used: 
            continue

        if check_above and check_left:
            res = tile_fits_below(grid[row-1][col], curr) and tile_fits_right(grid[row][col-1], curr)
            if res:
                grid[row][col] = curr
                used2 = used[:] + [curr]
                assemble_image3(tiles, grid, used2, size)  
        elif check_above:
            res = tile_fits_below(grid[row-1][col], curr)
            if res:
                grid[row][col] = curr
                used2 = used[:] + [curr]
                assemble_image3(tiles, grid, used2, size)  
        elif check_left:
            res = tile_fits_right(grid[row][col-1], curr)
            if res:
                grid[row][col] = curr
                used2 = used[:] + [curr]
                assemble_image3(tiles, grid, used2, size)  


def assemble_image2(corner_tile, tiles, size):
    grid = [[None for i in range(size)] for j in range(size)]
    used = []
    
    grid[0][0] = corner_tile
    used.append(corner_tile)
    assemble_image3(tiles, grid, used[:], size)


def assemble_image(corner_tiles, tiles, size):
    for c in corner_tiles:
        # Nasty
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()
        c.doflip()
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()
        assemble_image2(c, tiles, size)
        c.rotate()


def part1(tiles):
    # The edge values are unique, so all appear twice 
    all_edge_values = {}
    for t in tiles:
        edge_values = t.all_edge_values()
        for e in edge_values:
            if e in all_edge_values:
                all_edge_values[e] += 1
            else:
                all_edge_values[e]  = 1

    sides = {x for x in all_edge_values if all_edge_values[x] == 1}

    result = 1
    for t in tiles:
        if sum([True if s in sides else False for s in t.edge_values()]) == 2:
            # t is a corner tile
            result *= t.id
    return result       


def part2(tiles):
    # The edge values are unique, so all appear twice 
    all_edge_values = {}
    for t in tiles:
        edge_values = t.all_edge_values()
        for e in edge_values:
            if e in all_edge_values:
                all_edge_values[e] += 1
            else:
                all_edge_values[e]  = 1

    sides = {x for x in all_edge_values if all_edge_values[x] == 1}

    corners = []
    for t in tiles:
        if sum([True if s in sides else False for s in t.edge_values()]) == 2:
            # t is a corner tile
            corners.append(t)

    return assemble_image(corners, tiles, int(math.sqrt(len(tiles) + 1)))        


def solution(file):
    print("Input: ", file)
    data = ut.read_lines(file, True)

    tiles = []
    i    = 0
    tile = None
    while i < len(data):
        line = data[i]
        if line.startswith('Tile'):
            tile      = Tile()
            tile.bits = []
            tile.id   = int(line.split()[1][0:-1])
            for j in range(10):
                i += 1
                line = data[i]
                tile.bits = tile.bits + [x for x in line.replace('.', '0').replace('#', '1')]
            tiles.append(tile)
        i += 1 

    p1 = part1(tiles)
    print("Part1: ", p1)
    p2 = part2(tiles)


def main():
    #solution("day20-test.txt")    
    solution("day20-input.txt")


if __name__ == '__main__':
    main()

