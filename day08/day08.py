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
                m = dy/dx
                c = a[1] - m*a[0]
                for col in range(0, ncol):
                    row = m*col + c
                    if (row - int(row) < 0.00000000000001 and
                        row >= 0                           and
                        row < nrow):
                        antinode2.add((row,col))
                    
print('Part 1:', len(antinode1))
print('Part 2:', len(antinode2))

# Test input works, part 2 input does not
# An integer test precision problem?
# 982  is too low
# using:  row == int(row)
# 1070 is too high
# using: row - int(row) < 0.00001
# 991  is right answer for someone else
# 1064 is right answer for someone else
# using: row - int(row) < 0.000000000000001
