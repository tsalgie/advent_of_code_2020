def preamble_sum(numbers):
    for number in numbers[:-1]:
        if numbers[-1] - number in numbers[:-1]:
            return True
    return False

def encoding_error_01(numbers, preamble_length):
    if preamble_sum(numbers[:preamble_length+1]):
        return encoding_error_01(numbers[1:], preamble_length)
    else:
        return numbers[preamble_length]

def encoding_error_02(numbers, end, invalid_number):
    start = 0
    while(True):
        current_sum = sum(numbers[start:end])
        if current_sum == invalid_number:
            return min(numbers[start:end]) + max(numbers[start:end])
        elif current_sum < invalid_number:
            end += 1
        elif current_sum > invalid_number:
            start += 1

if __name__ == "__main__":
    with open('input.txt') as f:
        contents = [int(l.strip()) for l in f.readlines()]

    with open('output.txt', 'w') as f:
        encoding_error = encoding_error_01(contents, 25) 
        f.write("Part one: {}\n".format(encoding_error))
        f.write("Part one: {}\n".format(encoding_error_02(contents[:], 25, encoding_error)))
