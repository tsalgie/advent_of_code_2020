def handheld_halting_01(ops, tag):
    accumulator = 0
    index = 0
    while(index < len(ops) and ops[index][2] != tag):
        ops[index][2] = tag
        if ops[index][0] == 'nop':
            index += 1
        elif ops[index][0] == 'acc':
            accumulator += int(ops[index][1])
            index += 1
        elif ops[index][0] == 'jmp':
            index += int(ops[index][1])
    return (index, accumulator)

def handheld_halting_02(ops):
    jmpnop = lambda x : 'jmp' if x == 'nop' else 'nop'
    flopped = lambda x : ops[:x] + [[jmpnop(ops[x][0])] + ops[x][1:]] + ops[x + 1:]
    for index, op in enumerate(ops):
        answer = handheld_halting_01(flopped(index), index) if op[0] in ['jmp', 'nop'] else (None, None)
        if answer[0] == len(ops):
            return answer[1]

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [x.strip().split()+[None] for x in f.readlines()]
    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(handheld_halting_01(contents, False)[1]))
        f.write("Part two: {}\n".format(handheld_halting_02(contents)))
