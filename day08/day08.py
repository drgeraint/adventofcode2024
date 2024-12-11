#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrow = len(lines)
ncol = len(lines[0])

antennae  = dict()
antinode1 = set()
antinode2 = set()

row = 0
for line in lines:
    for col in range(0, ncol):
        c = line[col]
        if c != '.':
            if c not in antennae:
                antennae[c] = set()
            antennae[c].add((row,col))
    row += 1

for freq in antennae:
    for a in antennae[freq]:
        for b in antennae[freq]:
            if a != b:
                dx = b[0]-a[0]
                dy = b[1]-a[1]
                e = (a[0]-dx,a[1]-dy)
                f = (b[0]+dx,b[1]+dy)
                for n in [e,f]:
                    if (n[0] >= 0   and
                        n[0] < ncol and
                        n[1] >= 0   and
                        n[1] < nrow):
                        antinode1.add(n)
                for m in range(min(-nrow,-ncol),
                               max( nrow, ncol)):
                    e = (a[0]-m*dx,a[1]-m*dy)
                    f = (b[0]+m*dx,b[1]+m*dy)
                    for n in [e,f]:
                        if (n[0] >= 0   and
                            n[0] < ncol and
                            n[1] >= 0   and
                            n[1] < nrow):
                            antinode2.add(n)
                    
print('Part 1:', len(antinode1))
print('Part 2:', len(antinode2))

