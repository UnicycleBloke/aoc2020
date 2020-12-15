def run(data, count):
    mem   = {}
    idx   = 0
    prev  = 0

    for i in data:
        mem[i] = [idx, idx]
        idx   += 1
        prev   = i

    while idx < count:
        if mem[prev][0] == mem[prev][1]:
            prev = 0
        else:
            last = mem[prev][1] - mem[prev][0]
            prev = last

        if prev in mem:
            mem[prev][0] = mem[prev][1]
            mem[prev][1] = idx
        else:
            mem[prev] = [idx, idx]    
        idx += 1

    return prev 

data = [19,20,14,0,9,1]
print("Part 1:", run(data, 2020))
print("Part 2:", run(data, 30000000))
