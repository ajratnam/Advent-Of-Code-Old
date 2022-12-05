import re
from copy import deepcopy as copy

with open('inputs/input05.txt', 'r') as input_file:
    raw_stacks, moves = input_file.read().split('\n\n')

*stacks, rows = raw_stacks.split('\n')
stacks = map(''.join, zip(*[st[1::4].ljust(int(rows.split(' ')[-1])) for st in stacks]))
stacks = [list(st.replace(' ', ''))[::-1] for st in stacks]
stacks_og = copy(stacks)

pattern = re.compile(r'move (\d+) from (\d+) to (\d+)')
moves = [list(map(int, x)) for x in pattern.findall(moves)]

# PART 1
for n, s, e in moves:
    for i in range(n):
        stacks[e-1].append(stacks[s-1].pop())

print('Part 1 Answer - ', end='')
print(''.join([x[-1] for x in stacks]))

# PART 2
for n, s, e in moves:
    stacks_og[e-1].extend(stacks_og[s-1][-n:])
    stacks_og[s-1] = stacks_og[s-1][:-n]

print('Part 2 Answer - ', end='')
print(''.join([x[-1] for x in stacks_og]))