def seat_id(seat):
    return int(seat[:7], 2) * 8 + int(seat[-3:], 2)

def binary_boarding(lines):
    return max([seat_id(seat) for seat in lines])

def binary_finding(lines):
    seat_index = next(i for i in range(len(lines) - 1) if int(lines[i+1], 2) - int(lines[i], 2) == 2) + 1
    return seat_id(lines[seat_index])

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = sorted([x.strip().replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1') for x in f.readlines()])

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(binary_boarding(contents)))
        f.write("Part two: {}\n".format(binary_finding(contents)))
