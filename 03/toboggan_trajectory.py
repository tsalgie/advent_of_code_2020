# def tree_encounters(slopes):
#     results = [0]*len(slopes)
#     x_indices = [0]*len(slopes)
#     with open('input.txt') as f:
#         for line_number, line in enumerate([line.strip() for line in f]):
#             # line = line.strip()
#             for slope in slopes:
#                 if line_number % slope[1] == 0:
#                     result += 1 if line[x] == '#' else 0
#                     results
            
#             # change the x_indices
#             x += 3
#             x = x - len(line) if x >= len(line) else x

def encounter(slope, file):
    result = 0
    x = 0
    for line_number, line in enumerate(file):
        if line_number % slope[1] != 0:
            continue
        line = line.strip()
        result += 1 if line[x] == '#' else 0
        x += slope[0]
        x = x - len(line) if x >= len(line) else x
    return result

def encounters(slopes, file):
    results = []
    for slope in slopes:
        results.append(encounter(slope, file))
    
    mult = lambda l : l[0] * mult(l[1:]) if len(l) > 1 else l[0]
    return mult(results)



if __name__ == "__main__":
    lines = None
    with open('input.txt') as f:
        lines = f.readlines()
    
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    
    result_01 = encounter((3, 1), lines)
    result_02 = encounters(slopes, lines)

    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(result_01))
        f.write("Part two: {}\n".format(result_02))
