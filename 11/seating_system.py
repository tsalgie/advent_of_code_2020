def seating_systm_01(waiting_area):
    while(True):
        occupied = 0
        changed = 0
        for r, row in enumerate(waiting_area):
            for c, seat in enumerate(row):
                if seat[0] == '#':
                    y = r - 1
                    x = c - 1
                    for i in range(y, y + 3):
                        for j in range(x, x + 3):
                            if (i == r and j == c) or (i < 0 or j < 0) or (i >= len(waiting_area) or j >= len(row)):
                                continue
                            waiting_area[i][j][1] += 1

        for r, row in enumerate(waiting_area):
            for c, seat in enumerate(row):
                if seat[0] == 'L' and seat[1] == 0:
                    waiting_area[r][c][0] = '#'
                    changed += 1
                elif seat[0] == '#' and seat[1] > 3:
                    waiting_area[r][c][0] = 'L'
                    changed += 1
                if waiting_area[r][c][0] == '#':
                    occupied += 1
                waiting_area[r][c][1] = 0
        if changed == 0:
            return occupied

def check_seats(seat, waiting_area, rule):
    to_check = seat[:]
    while(True):
        to_check[0] += rule[0]
        to_check[1] += rule[1]
        if (to_check[0] < 0 or to_check[1] < 0) or (to_check[0] >= len(waiting_area) or to_check[1] >= len(waiting_area[0])):
            return 0
        if waiting_area[to_check[0]][to_check[1]][0] == '#':
            return 1
        if waiting_area[to_check[0]][to_check[1]][0] == 'L':
            return 0
     
def check_seat(seat, waiting_area, checker):
    rules = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
    return sum([checker(seat, waiting_area, rule) for rule in rules])

def seating_systm_02(waiting_area):
    while(True):
        occupied = 0
        changed = 0
        for r, row in enumerate(waiting_area):
            for c, seat in enumerate(row):
                waiting_area[r][c][1] = check_seat([r, c], waiting_area, check_seats)

        for r, row in enumerate(waiting_area):
            for c, seat in enumerate(row):
                if seat[0] == 'L' and seat[1] == 0:
                    waiting_area[r][c][0] = '#'
                    changed += 1
                elif seat[0] == '#' and seat[1] > 4:
                    waiting_area[r][c][0] = 'L'
                    changed += 1
                if waiting_area[r][c][0] == '#':
                    occupied += 1
                waiting_area[r][c][1] = 0
        if changed == 0:
            return occupied

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.readlines()

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(seating_systm_01([[[c, 0] for c in l.strip()] for l in lines])))
        f.write("Part two: {}\n".format(seating_systm_02([[[c, 0] for c in l.strip()] for l in lines])))
