import sys
import re


def part1(docs):
    print('Part 1')

    # TODO Use data structure
    valid = 0
    for doc in docs:
        print(doc)
        fields = doc.split()
        keys = []
        for field in fields:
            keys.append(field.split(':')[0])

        print(keys)  
        good = 'ecl' in keys and 'pid' in keys and 'eyr' in keys and 'hcl' in keys and 'byr' in keys and 'iyr' in keys and 'hgt' in keys #and 'cid' in keys 

        if good == True:
            valid = valid + 1    

    print ('Valid:', valid)


def is_field_valid(key, value):
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    if key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif key == 'pid':
        m = re.match('\d{9}', value)
        if m == None:
            return False

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif key == 'eyr':
        m = re.match('\d{4}', value)
        if m == None:
            return False
        if int(value) < 2020 or int(value) > 2030:
            return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif key == 'hcl': 
        m = re.match('#[0-9a-f]{6}', value)
        if m == None:
            return False

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    elif key == 'byr': 
        m = re.match('\d{4}', value)
        if m == None:
            return False
        if int(value) < 1920 or int(value) > 2002:
            return False

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif key == 'iyr':
        m = re.match('\d{4}', value)
        if m == None:
            return False
        if int(value) < 2010 or int(value) > 2020:
            return False

    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    elif key == 'hgt':
        m = re.match('(\d+)cm', value)
        if m == None:
            m = re.match('(\d+)in', value)
            if m == None:
                return False
            if int(m.group(1)) < 59 or int(m.group(1)) > 76:
                return False
        else:                
            if int(m.group(1)) < 150 or int(m.group(1)) > 193:
                return False

    return True


def is_present_and_valid(key, map):
    if not key in map:
        print('%s missing' % (key))
        return False
    elif not is_field_valid(key, map[key]):
        print('%s invalid = %s' % (key, map[key]))
        return False
    return True


def is_passport_valid(doc):
    temp   = doc.split()
    fields = {}
    for t in temp:
        s = t.split(':')
        fields[s[0]] = s[1]

    print(fields)

    valid = True
    valid = valid and is_present_and_valid('pid', fields)
    valid = valid and is_present_and_valid('ecl', fields)
    valid = valid and is_present_and_valid('eyr', fields)
    valid = valid and is_present_and_valid('byr', fields)
    valid = valid and is_present_and_valid('iyr', fields)
    valid = valid and is_present_and_valid('hgt', fields)
    valid = valid and is_present_and_valid('hcl', fields)

    print('Passport valid:', valid)
    print()

    return valid        


def part2(docs):
    print('Part 2')

    valid = 0
    for doc in docs:
        if is_passport_valid(doc):
            valid = valid + 1

    print('Valid:', valid)


def solution(filename):
    print('Input file : {}'.format(filename))
    file = open(filename)
    lines = file.readlines()

    # TODO Create data structure
    docs = []
    doc  = ''
    for line in lines:
        text = line.strip()
        if len(text) == 0:
            docs.append(doc)
            doc = ''
        else:
            doc = doc + text + ' '
    if len(doc) > 0:        
        docs.append(doc)

    #for d in docs:
    #    print(d)

    #part1(docs)
    part2(docs)


def main():
    print('AOC problem #4')
    if len(sys.argv) < 2:
        print('Supply at least one input file name')
        exit(1)

    for filename in sys.argv[1:]:
        solution(filename)
    

if __name__ == '__main__':
    # Execute only if run as a script
    main()
