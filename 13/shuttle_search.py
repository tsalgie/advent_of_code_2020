def shuttle_search_01(lines):
    time, busses = int(lines[0]), sorted(map(lambda x : int(x), filter(lambda x : x != 'x', lines[1].strip().split(','))))
    while True:
        for bus in busses:
            if time % bus == 0:
                return ((time - int(lines[0])) * bus)
        time += 1        

def shuttle_search_02(lines):
    busses = [(int(bus), i) for i, bus in enumerate(lines[1].split(',')) if bus != 'x']
    time = busses[0][0]
    increment = 1
    while True:
        current_bus = 0
        this_increment = 1
        for i, bus in enumerate(busses):
            if (time + bus[1]) % bus[0] != 0:
                break
            this_increment *= bus[0]
            current_bus = i
        if current_bus == len(busses) - 1:
            return time
        else:
            increment = max(increment, this_increment)
            time += increment

with open('input.txt') as f:
    lines = list(f.readlines())

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(shuttle_search_01(lines)))
        f.write("Part one: {}\n".format(shuttle_search_02(lines)))
