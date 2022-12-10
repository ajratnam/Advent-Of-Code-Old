with open('inputs/input09.txt', 'r') as input_file:
    moves = list(map(str.split, input_file.read().split('\n')))

dirs = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def move(hp, tp):
    diff = hp[0] - tp[0], hp[1] - tp[1]
    abd = [*map(abs, diff)]

    if 2 in abd:
        i2 = abd.index(2)
        tp[i2] += diff[i2] // 2
        if 1 in abd:
            tp[i2^1] += diff[i2^1]
        else:
            tp[i2^1] += diff[i2^1] // 2

def rope(num):
    pos, knots = {(0, 0)}, [[0, 0] for _ in range(num)]
    for drc, ti in moves:
        for _ in range(int(ti)):
            knots[0][0] += dirs[drc][0]
            knots[0][1] += dirs[drc][1]
            for i in range(num-1):
                move(*knots[i:i+2])
            pos.add(tuple(knots[-1]))
    return len(pos)

# PART 1
print('Part 1 Answer - ', end='')
print(rope(2))

# PART 2
print('Part 2 Answer - ', end='')
print(rope(10))