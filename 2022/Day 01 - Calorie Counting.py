with open('inputs/input01.txt', 'r') as input_file:
    all_calories = input_file.read().split('\n'*2)

calories = sorted([sum(map(int, line.split('\n'))) for line in all_calories])

# PART 1
print('Part 1 Answer - ', end='')
print(calories[-1])

# PART 2
print('Part 2 Answer - ', end='')
print(sum(calories[-3:]))
