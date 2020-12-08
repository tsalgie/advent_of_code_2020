# The bags dict will be like mirrored beige: ['pale lavender', 'mirrored olive', 'mirrored tomato']
def handy_haverscape_01(lines):
    bags = dict()
    for line in (line.split() for line in lines):
        bag_list = [' '.join(line[i * 4 + 1:i * 4 + 3]) for i in range(1, len(line) // 4)]
        for contained in bag_list:
            bags[contained] = (bags.get(contained) or []) + [' '.join(line[:2])]

    contains = []
    current = {'shiny gold'}
    while(len(current) != 0):
        acc = set()
        for bag in current:
            if bag not in contains:
                contains.append(bag)
                current.add(bag)
                acc = acc.union(bags[bag]) if bag in bags else acc
        current = acc
    return len(contains) - 1

# The bags dict will be like {mirrored beige: [('4', 'pale lavender'), ('2', 'mirrored olive'), ('3', 'mirrored tomato')]}
def handy_haverscape_02(lines):
    bags = {' '.join(line[:2]): [(int(line[i*4]), ' '.join(line[i * 4 + 1:i * 4 + 3])) for i in range(1, len(line) // 4)] for line in (line.split() for line in lines)}
    bags_count = lambda target : sum(bag[0] * bags_count(bag[1]) for bag in bags[target]) + 1
    return bags_count('shiny gold') - 1


if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [l[:-2] for l in f.readlines()]

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(handy_haverscape_01(contents)))
        f.write("Part one: {}\n".format(handy_haverscape_02(contents)))
