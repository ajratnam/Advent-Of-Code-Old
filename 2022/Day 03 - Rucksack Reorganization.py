from string import ascii_letters as letters

with open('inputs/input03.txt', 'r') as input_file:
    rucksacks = input_file.read().splitlines()

# PART 1
sacks = [''.join({*sack[:len(sack)//2]} & {*sack[len(sack)//2:]}) for sack in rucksacks]

print('Part 1 Answer - ', end='')
print(sum(map(letters.index, sacks))+len(sacks))

# PART 2
sacks = [[*set.intersection(*map(set, rucksacks[i:i+3]))][0] for i in range(0, len(rucksacks), 3)]
print('Part 2 Answer - ', end='')
print(sum(map(letters.index, sacks))+len(sacks))
