with open('inputs/input06.txt', 'r') as input_file:
    stream = input_file.read()


def get_mark(num):
    for i in range(len(stream)):
        if len(set(stream[i:i+num])) >= num:
            return i+num


# PART 1
print('Part 1 Answer - ', end='')
print(get_mark(4))

# PART 2
print('Part 2 Answer - ', end='')
print(get_mark(14))
