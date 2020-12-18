def adjacent_cubes(cube):
    d = [int(c) for c in cube.split(',')]
    for z in range(d[0]-1, d[0]+2):
        for r in range(d[1]-1, d[1]+2):
            for c in range(d[2]-1, d[2]+2):
                adjacent = "{},{},{}".format(z,r,c)
                if adjacent == cube:
                    continue 
                yield adjacent

def adjacent_hypercubes(cube):
    d = [int(c) for c in cube.split(',')]
    for w in range(d[0]-1, d[0]+2):
        for z in range(d[1]-1, d[1]+2):
            for r in range(d[2]-1, d[2]+2):
                for c in range(d[3]-1, d[3]+2):
                    adjacent = "{},{},{},{}".format(w,z,r,c)
                    if adjacent == cube:
                        continue 
                    yield adjacent

def generate_count(state, adjacency_func):
    count = dict()
    for cube_coords, cube_state in state.items():
        if cube_state == '#':
            for cube in adjacency_func(cube_coords):
                count[cube] = count[cube] + 1 if cube in count else 1
    return count

def generate_state(count, current_state):
    state = dict()
    for cube_coords, num_adjacent in count.items():
        if cube_coords in current_state and current_state[cube_coords] == '#' and 2 <= num_adjacent <= 3:
            state[cube_coords] = '#'
        elif cube_coords in current_state and current_state[cube_coords] == '#' and  not 2 <= num_adjacent <= 3:
            state[cube_coords] = '.'
        elif (cube_coords not in current_state or current_state[cube_coords] == '.') and num_adjacent == 3:
            state[cube_coords] = '#'
        else:
            state[cube_coords] = '.'
    for cube_coords in set(current_state.keys())-set(count.keys()):
        state[cube_coords] = '.'
    return(state)

def conway_cubes(iterations, state, adjacency_func):
    count = None
    for _ in range(iterations):
        count = generate_count(state, adjacency_func)
        state = generate_state(count, state)
    return sum([1 if i == '#' else 0 for i in state.values()])

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = list(f.readlines())

    starting_state = dict()
    starting_hyperstate = dict()

    for r, row in enumerate(contents):
        for c, col in enumerate(row.strip()):
            starting_state["{},{},{}".format(0,r,c)] = col
            starting_hyperstate["{},{},{},{}".format(0,0,r,c)] = col
    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(conway_cubes(6, starting_state, adjacent_cubes)))
        f.write("Part one: {}\n".format(conway_cubes(6, starting_hyperstate, adjacent_hypercubes)))
