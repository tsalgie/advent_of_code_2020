import re

if __name__ == "__main__":
    # each line split into elements: first number, second number, character, password
    passwords = None
    with open('input.txt') as f:
        passwords = list(map(lambda line : re.split(' |-|: ', line.strip()), f.readlines()))

    first_count = sum(map(lambda p: int(p[0]) <= p[3].count(p[2]) <= int(p[1]), passwords))
    second_count = sum(map(lambda p: (p[3][int(p[0])-1] == p[2]) != (p[3][int(p[1])-1] == p[2]), passwords))

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(first_count))
        f.write("Part two: {}\n".format(second_count))
