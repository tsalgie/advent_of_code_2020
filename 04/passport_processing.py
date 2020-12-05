def valid_passports_01(lines):
    num_valid = 0    
    current_line = ''
    for line in lines:
        if line == '\n':
            count = current_line.count(' ')
            num_valid += 1 if count == 8 or (count == 7 and 'cid:' not in current_line) else 0
            current_line = ''
        else:
            current_line += " {}".format(line.strip())
    return num_valid

def valid_passports_02(lines):
    validators = {
        'byr': lambda x : len(x) == 4 and 1920 <= int(x) <= 2002,
        'iyr': lambda x : len(x) == 4 and 2010 <= int(x) <= 2020,
        'eyr': lambda x : len(x) == 4 and 2020 <= int(x) <= 2030,
        'hgt': lambda x : (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76) or (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193),
        'hcl': lambda x : x[0] == '#' and set(x[1:]).issubset(set('abcdef0123456789')),
        'ecl': lambda x : x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda x : len(x) == 9 and x.isdigit(),
        'cid': lambda _ : True
    }

    num_valid = 0    
    current_line = ''
    for line in lines:
        if line == '\n':
            fields = dict({key:val for key, val in [field.split(':') for field in current_line.strip().split()]}, **{'cid': None})
            num_valid += 1 if sum(map(lambda x : validators[x[0]](x[1]), fields.items())) == 8 else 0
            current_line = ''
        else:
            current_line += " {}".format(line.strip())
    return num_valid

if __name__ == "__main__":
    contents = None
    with open('input.txt') as f:
        contents = f.readlines() + ['\n']

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(valid_passports_01(contents)))
        f.write("Part two: {}\n".format(valid_passports_02(contents)))
