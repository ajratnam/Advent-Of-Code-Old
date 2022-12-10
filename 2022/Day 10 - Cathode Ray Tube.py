with open('inputs/input10.txt', 'r') as input_file:
	instr = input_file.read().replace('noop', '0').replace('addx ', '').split('\n')

rv = [1]
for i, v in enumerate(map(int, instr)):
	rv += [rv[-1],rv[-1]+v] if v else [rv[-1]]

# PART 1
print('Part 1 Answer - ', end='')
print(sum(rv[i-1]*i for i in range(20,len(rv),40)))

# PART 2
print('Part 2 Answer - ')
rv = [".#"[x-1<=i%40<=x+1] for i, x in enumerate(rv)]
nrv = [rv[i*40:(i+1)*40] for i in range(len(rv)//40)]
dup = lambda n:lambda x:sum([*zip(*[x]*n)],())
print(*map(''.join, dup(2)([*map(dup(4), nrv)])), sep='\n')