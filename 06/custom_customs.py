def custom_customs(lines, operation):
    count = 0    
    current_line = None
    for line in lines:
        if line == '':
            count += len(current_line)
            current_line = None
        else:
            current_line = set(line) if current_line == None else operation(current_line, line)
    return count    

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [x.strip() for x in f.readlines()]+['']

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(custom_customs(contents, set.union)))
        f.write("Part two: {}\n".format(custom_customs(contents, set.intersection)))
