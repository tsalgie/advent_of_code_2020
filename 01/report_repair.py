def two_product(numbers, value):
    #Partition the list by finding the index of the largest number < 1/2 the value
    partition_index = next(i for i, val in enumerate(numbers) if val >= value / 2)
    exclusion_index = partition_index
    for large in numbers[partition_index:]:
        for i, small in enumerate(numbers[:exclusion_index]):
            if large + numbers[i] > value:
                exclusion_index = i
            if large + small == value:
                return large * numbers[i]
    return None

def three_product(numbers, value):
    # Do an initial partition to find the largest of the smallest 3 numbers close to the value
    partition_index = next(i for i in range(len(numbers) - 2) if numbers[i] + numbers[i+1] + numbers[i + 2] >= value) + 1

    for i in range(partition_index, len(numbers)):
        result = two_product(numbers[:i], value - numbers[i])
        if result != None:
            return result * numbers[i]

if __name__ == "__main__":
    contents = None
    with open('input.txt') as f:
        contents = sorted(map(lambda x : int(x.strip()), f.readlines()))
    first_answer = two_product(contents, 2020)
    second_answer = three_product(contents, 2020)
    with open('output.txt', 'w') as f:
        f.write("Part one: {}\n".format(first_answer))
        f.write("Part two: {}\n".format(second_answer))
