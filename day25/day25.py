def transform(value, subject):
    return (value * subject) % 20201227


def find_loopsize(key):
    size  = 0
    value = 1
    while True:
        if value == key:
            return size
        value = transform(value, 7)
        size += 1


def encryption_key(pubkey, loopsize):
    key = 1  
    for i in range(loopsize):
        key = transform(key, pubkey)
    return key


def part1(card_key, door_key):
    print('Part1: ')

    card_loops = find_loopsize(card_key)
    print('card_loops', card_loops)

    door_loops = find_loopsize(door_key)
    print('door_loops', door_loops)

    key1 = encryption_key(card_key, door_loops)
    #key2 = encryption_key(door_key, card_loops)
    print(key1)


def main():
    # Test
    #part1(5764801, 17807724)
    # Input
    part1(14205034, 18047856)


if __name__ == '__main__':
    main()
