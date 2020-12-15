def docking_data_01(lines):
    mask = None
    data = dict()
    for line in [line.split() for line in lines]:
        if line[0] == 'mask':
            mask = line[2]
        else:
            index = line[0]
            bits = "{0:b}".format(int(line[2]))
            bits = (36-len(bits))*'0' + bits
            masked = []
            for i, c in enumerate(bits):
                if mask[i] != 'X':
                    masked.append(mask[i])
                else:
                    masked.append(c)
            data[index] = ''.join(masked)
    return sum([int(v, 2) for v in data.values()])

def bitmask_02(address, mask):
    bits = "{0:b}".format(int(address))
    bits = (len(mask)-len(bits))*'0' + bits
    masked = []
    result = []
    for i, c in enumerate(bits):
        if mask[i] == 'X':
            result.append(None)
            masked.append(i)
        elif mask[i] == '1':
            result.append('1') 
        else:
            result.append(c)
    # Now we have the final bit template, and a list of masked indices.
    # loop over 2^len(masked) in binary to come up with all permutations
    results = []
    for i in range(pow(2, len(masked))):
        bits = list("{0:b}".format(i))
        bits = (len(masked)-len(bits))*['0'] + bits
        cur = []
        for c in reversed(result):
            if c == None:
                cur.append(bits.pop())
            else:
                cur.append(c)
        cur.reverse()
        results.append(int(''.join(cur), 2))
    return results

def docking_data_02(lines):
    mask = None
    data = dict()
    for line in [line.split() for line in lines]:
        if line[0] == 'mask':
            mask = line[2]
        else:
            address = line[0].split('[')[1][:-1]
            addresses = bitmask_02(address, mask)
            for a in addresses:
                data[a] = line[2]
    return sum([int(v) for v in data.values()])

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [l.strip() for l in f.readlines()]
        
    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(docking_data_01(contents)))
        f.write("Part two: {}\n".format(docking_data_02(contents)))

# There is some refactoring that can be done here, in addition to some good old cleanup and simplification, but I'm out of time.