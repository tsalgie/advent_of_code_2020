def rambunctious_recitation(numbers, target):
    history = {n: i + 1 for i, n in enumerate(numbers)}
    turn = len(history) + 1
    number = 0
    while turn < target:
        if number in history:
            history[number], number = turn, turn - history[number]
        else:
            history[number] = turn
            number = 0
        turn += 1
    return number

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [int(i) for i in list(f.readlines())[0].strip().split(',')]

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(rambunctious_recitation(contents, 2020)))
        f.write("Part one: {}\n".format(rambunctious_recitation(contents, 30000000)))
