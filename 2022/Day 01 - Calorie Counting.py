with open('inputs/input01.txt', 'r') as input_file:
    val = input_file.read().split('\n'*2)

calories = [sum(map(int, line.split('\n'))) for line in val]

# PART 1
print('Part 1 Answer - ', end='')
print(max(calories))

# PART 2
print('Part 2 Answer - ', end='')
print(sum(sorted(calories)[-3:]))
