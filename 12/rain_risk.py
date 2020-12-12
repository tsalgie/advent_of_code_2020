def rain_risk_01(instructions):
    start = {'N': 0, 'E': 0, 'S': 0, 'W': 0, 'L': 0, 'R': 0, 'F': 0}
    degrees = {270: 'N', 0: 'E', 90: 'S', 180: 'W'}
    facing = 0
    for instruction in instructions:
        start[instruction[0]] += instruction[1]
        if instruction[0] == 'R':
            facing = (facing + instruction[1]) % 360
        elif instruction[0] == 'L':
            facing = (facing - instruction[1]) % 360
        elif instruction[0] == 'F':
            start[degrees[facing]] += instruction[1]
    return abs(start['N']-start['S']) + abs(start['E']-start['W'])

def rain_risk_02(instructions):
    waypoint = {'N': 1, 'E': 10, 'S': 0, 'W': 0, 'L': 0, 'R': 0, 'F': 0}
    index = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
    start = {'N': 0, 'E': 0, 'S': 0, 'W': 0, 'L': 0, 'R': 0, 'F': 0}
    degrees = {270: 'N', 0: 'E', 90: 'S', 180: 'W'}
    for instruction in instructions:
        waypoint[instruction[0]] += instruction[1]
        if instruction[0] == 'R':
            for i in range(instruction[1]//90):
                waypoint = {'N': waypoint['W'], 'E': waypoint['N'], 'S': waypoint['E'], 'W': waypoint['S'], 'L': 0, 'R': 0, 'F': 0}
        elif instruction[0] == 'L':
            for i in range(instruction[1]//90):
                waypoint = {'N': waypoint['E'], 'E': waypoint['S'], 'S': waypoint['W'], 'W': waypoint['N'], 'L': 0, 'R': 0, 'F': 0}
        elif instruction[0] == 'F':
            #waypoint = {max(0, waypoint[w[0]] - waypoint[w[1]]) for w in [('N','S'),('S','N'),('E','W'),('W','E')]}  
            waypoint['N'], waypoint['S'], waypoint['E'], waypoint['W'] = max(0, waypoint['N'] - waypoint['S']), max(0, waypoint['S'] - waypoint['N']), max(0, waypoint['E'] - waypoint['W']), max(0, waypoint['W'] - waypoint['E'])
            for d in ['N','S','E','W']:
                start[d] += waypoint[d] * instruction[1]
            print(waypoint)
            print(start)

    return abs(start['N']-start['S']) + abs(start['E']-start['W'])

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [(l[0], int(l[1:])) for l in f.readlines()]

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(rain_risk_01(contents)))
        f.write("Part two: {}\n".format(rain_risk_02(contents)))

#Part one: 1221
#Part two: 59435