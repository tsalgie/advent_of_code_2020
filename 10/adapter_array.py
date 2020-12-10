def adapter_array_01(jolts):
    differences = [0, 0, 1]
    for i in range(len(jolts) - 1):
        differences[jolts[i + 1] - jolts[i] - 1] += 1
    return differences[0] * differences[2]

def adapter_array_02(jolts):
    groups = [True if jolts[i + 2] - jolts[i] <= 3 else False for i in range(len(jolts) - 2)]
    group_counts = [0]
    for g in groups:
        if g:
            group_counts[-1] += 1
        else:
            group_counts += [0] if group_counts[-1] != 0 else []
    mult = lambda l : l[0] * mult(l[1:]) if len(l) > 1 else l[0]
    valid_subchains = lambda length : len(["{0:b}".format(i) for i in range(pow(2, length)) if '111' not in "{0:b}".format(i)])
    return mult(list(map(valid_subchains, group_counts)))

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = sorted([int(l.strip()) for l in f.readlines()])

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(adapter_array_01([0] + contents)))
        f.write("Part two: {}\n".format(adapter_array_02([0] + contents + [contents[-1] + 3])))