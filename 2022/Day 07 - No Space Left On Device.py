from collections import defaultdict as dir_dict
import re

with open('inputs/input07.txt', 'r') as input_file:
    console = re.findall(r'\$ (.*)\n([^$]*)', input_file.read())

cdir, dirs, dirsz = '', dir_dict(dict), {}

def cwd():
    return cdir or '/'

for command, output in console:
    if command[:2] == 'cd':
        ndir = command.split()[1]
        if ndir == '..':
            cdir = cdir[:cdir.rfind('/')]
        elif ndir == '/':
            cdir = ''
        else:
            cdir += f'/{ndir}'
        continue
    output = re.findall(r'(.*) (.*)\n?', output)
    for size, file in output:
        dirs[cwd()][file] = f'{cdir}/{file}' if size == 'dir' else int(size)

def get_size(path):
    total_size = 0
    for filesize in dirs[path].values():
        if isinstance(filesize, str):
            filesize = get_size(filesize)
        total_size += filesize
    dirsz[path] = total_size
    return total_size

needed = get_size('/') - 4 * 10 ** 7
sizes = sorted(dirsz.values())

# PART 1
print('Part 1 Answer - ', end='')
print(sum(filter((10**5).__ge__, sizes)))

# PART 2
print('Part 2 Answer - ', end='')
print(next(filter(needed.__lt__, sizes)))
