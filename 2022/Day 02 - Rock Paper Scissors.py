from itertools import product as permutations

with open('inputs/input02.txt', 'r') as input_file:
    matches = input_file.read().translate({88: 65, 89: 66, 90: 67}).splitlines()

out = tuple('ACBA')

move_move_table = {}
move_outcome_table = {}

for other, self in permutations('ABC', repeat=2):
    outcome = {self: 'B', out[out.index(self)+1]: 'C'}.get(other, 'A')
    score = ord(self) + 3 * ord(outcome) - 259
    move_move_table[(other, self)] = score
    move_outcome_table[(other, outcome)] = score

get_sum = lambda table: sum([table[(*match.split(),)] for match in matches])

# PART 1
print('Part 1 Answer - ', end='')
print(get_sum(move_move_table))

# PART 2
print('Part 2 Answer - ', end='')
print(get_sum(move_outcome_table))
