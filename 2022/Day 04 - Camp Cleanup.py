import re

pair = re.compile(r'(\d+)-(\d+),(\d+)-(\d+)')

with open('inputs/input04.txt', 'r') as input_file:
    pairs = [list(map(int,x)) for x in pair.findall(input_file.read())]

# PART 1
print('Part 1 Answer - ', end='')
print(len([1 for pair in pairs if (pair[0]==pair[2])|(pair[1]==pair[3])|(pair[0]>pair[2])^(pair[1]<pair[3])^1]))

# PART 2
print('Part 2 Answer - ', end='')
print(len([1 for pair in pairs if ((pair[0]>pair[3])|(pair[1]<pair[2]))^1]))
