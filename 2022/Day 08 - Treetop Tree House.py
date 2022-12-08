from math import prod

with open('inputs/input08.txt', 'r') as input_file:
    raw_terrain = input_file.read().split('\n')

terrain, seen = [[((r, c), h) for r, h in enumerate(cv)] for c, cv in enumerate(raw_terrain)], set()
def parse(elm):
    seen.add(elm[0][0])
    tallest = elm[0][1]
    for pos, height in elm[1:]:
        if height > tallest:
            tallest = height
            seen.add(pos)

# PART 1
for _ in range(2):
    for row in terrain:
        parse(row)
        parse(row[::-1])
    terrain = list(map(list, zip(*terrain)))

print('Part 1 Answer - ', end='')
print(len(seen))

# PART 2
terarray, paths = dict(sum(terrain, [])), [(0, -1), (-1, 0), (0, 1), (1, 0)]
def get_visible(rn, cn, path):
    count, tallest = 0, terarray[(rn, cn)]
    while True:
        rn, cn = rn + path[0], cn + path[1]
        if (rn, cn) not in terarray:
            break
        ch = terarray[(rn, cn)]
        count += 1
        if ch >= tallest:
            break
    return count

print('Part 2 Answer - ', end='')
print(max(prod(get_visible(row, col, path) for path in paths) for row, col in terarray))