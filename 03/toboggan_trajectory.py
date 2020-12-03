if __name__ == "__main__":
    result = 0
    with open('input.txt') as f:
        x = 0
        for line in f:
            line = line.strip()
            result += 1 if line[x] == '#' else 0
            x += 3
            x = x - len(line) if x >= len(line) else x

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(result))
