import sys
import re


def is_valid_year(value, lo, hi):
    m = re.match('^\d{4}$', value)
    if m != None:
        year = int(value)
        return year >= lo and year <= hi
    return False


def is_field_valid(key, value):
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    if key == 'byr': 
        return is_valid_year(value, 1920, 2002)

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    elif key == 'iyr':
        return is_valid_year(value, 2010, 2020)

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    elif key == 'eyr':
        return is_valid_year(value, 2020, 2030)

    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    elif key == 'hgt':
        hcm = re.match('^(\d+)cm$', value)
        if hcm != None:  
            h = int(hcm.group(1))
            return h >=150 and h <= 193
        hin = re.match('^(\d+)in$', value)
        if hin != None:  
            h = int(hin.group(1))
            return h >=59 and h <= 76
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    elif key == 'hcl': 
        m = re.match('^#[0-9a-f]{6}$', value)
        return m != None

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    elif key == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    elif key == 'pid':
        m = re.match('^\d{9}$', value)
        if m == None:
            print('pid invalid = "%s"' % (value))
        return m != None

    # cid (Country ID) - ignored, missing or not.
    elif key == 'cid':
        return True

    return True


def is_present(key, map):
    if not key in map:
        #print('%s missing' % (key))
        return False
    return True


def is_present_and_valid(key, map):
    if not is_present(key, map):
        return False
    elif not is_field_valid(key, map[key]):
        #print('%s invalid = "%s"' % (key, map[key]))
        return False
    return True


def is_passport_valid(doc, func):
    temp   = doc.split()
    fields = {}
    for t in temp:
        s = t.split(':')
        fields[s[0]] = s[1]

    valid = True
    valid = valid and func('pid', fields)
    valid = valid and func('ecl', fields)
    valid = valid and func('eyr', fields)
    valid = valid and func('byr', fields)
    valid = valid and func('iyr', fields)
    valid = valid and func('hgt', fields)
    valid = valid and func('hcl', fields)
    return valid        


def part1(docs):
    print('Part 1')
    valid = 0
    for doc in docs:
        if is_passport_valid(doc, is_present):
            valid = valid + 1
    print('Valid:', valid)


def part2(docs):
    print('Part 2')
    valid = 0
    for doc in docs:
        if is_passport_valid(doc, is_present_and_valid):
            valid = valid + 1
    print('Valid:', valid)


def solution(filename):
    print('Input file : {}'.format(filename))
    file = open(filename)
    lines = file.readlines()

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

    part1(docs)
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
