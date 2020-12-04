def tree_encounters(slopes, lines):
    results = [0]*len(slopes)
    x_indices = [0]*len(slopes)
    for line_number, line in enumerate(lines):
        # line = line.strip()
        for i, slope in enumerate(slopes):
            if line_number % slope[1] == 0:
                results[i] += 1 if line[x_indices[i]] == '#' else 0
                x_indices[i] += slope[0] if x_indices[i] + slope[0] < len(line) else slope[0] - len(line) 
    mult = lambda l : l[0] * mult(l[1:]) if len(l) > 1 else l[0]
    return mult(results)       

if __name__ == "__main__":
    lines = None
    with open('input.txt') as f:
        lines = list(map(lambda x : x.strip(), f.readlines()))

    result_01 = tree_encounters([(3, 1)], lines)
    result_02 = tree_encounters([(1,1),(3,1),(5,1),(7,1),(1,2)], lines)

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(result_01))
        f.write("Part two: {}\n".format(result_02))
