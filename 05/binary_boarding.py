def binary_boarding(lines):
    seats = [[(row, column) for column in range(8)] for row in range(128)]
    occupied_seats = [binary_seats(line, seats) for line in lines]
    answers = [seat[0]*8 + seat[1] for seat in occupied_seats]
    return max(answers)

def binary_seats(boarding_pass, seats):
    if isinstance(seats, tuple):
        return seats
    elif len(seats) == 1:
        return binary_seats(boarding_pass, seats[0])
    elif boarding_pass[0] == '0':
        return binary_seats(boarding_pass[1:], seats[:len(seats) // 2])
    elif boarding_pass[0] == '1':
        return binary_seats(boarding_pass[1:], seats[-len(seats) // 2:])

def binary_finding(lines):
    flatten = lambda l : l[0] + flatten(l[1:]) if len(l) > 1 else l[0]
    binary = lambda k : ['0'*(k-len(j))+j for j in ["{0:b}".format(i) for i in range(pow(2,k))]]
    seats = flatten([[row+column for column in binary(3)] for row in binary(7)])
    remaining = sorted(list(set(seats) - set(lines)))
    seat_index = next(i for i in range(len(remaining) - 2) if int(remaining[i+1], 2)-int(remaining[i], 2) != 1 and int(remaining[i+2], 2)-int(remaining[i+1], 2) != 1) + 1
    return int(remaining[seat_index][:7], 2) * 8 + int(remaining[seat_index][-3:], 2)

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [x.strip().replace('F', '0').replace('L', '0').replace('B', '1').replace('R', '1') for x in f.readlines()]

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(binary_boarding(contents)))
        f.write("Part two: {}\n".format(binary_finding(contents)))
