import re
from copy import deepcopy as copy

with open('inputs/input11.txt', 'r') as input_file:
	rmonkis = input_file.read()

monkis = [*map(list, re.findall(r's: (.*)\n.*= (.+)\n'+(r'.*y (\d+)\n'*3)[:-2], rmonkis))]
waste = 1
for monki in monkis:
	monki[0] = eval(f'[{monki[0]}]')
	monki[2:] = map(int, monki[2:])
	waste *= monki[2]
dpmonkis = copy(monkis)

def calculate(rounds, bias):
	tsum = [0]*len(monkis)
	for _ in range(rounds):
		for i, monki in enumerate(monkis):
			items, op, div, t, f = monki
			tsum[i] += len(items)
			while items:
				nv = eval(op.replace('old',str(items.pop(0))))%waste//bias
				monkis[[t,f][bool(nv%div)]][0].append(nv)
	monkis[::] = dpmonkis[::]
	return sorted(tsum)

# PART 1
print('Part 1 Answer - ', end='')
fsum = calculate(20, 3)
print(fsum[-1] * fsum[-2])

# PART 2
print('Part 2 Answer - ', end='')
fsum = calculate(10000, 1)
print(fsum[-1] * fsum[-2])