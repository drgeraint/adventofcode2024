#! /usr/bin/env python3

import sys
sys.setrecursionlimit(1000000)

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

if filename == 'test1.txt':
    ncols = 6+1
    nline = 12
else:
    ncols = 70+1
    nline = 1024
nrows = ncols

corrupt = set()
for i in range(0,nline):
    line = lines[i]
    x,y = [int(n) for n in line.split(',')]
    corrupt.add((x,y))

visited = set()
    
steps = dict()
steps[(0,0)] = 0

def explore(pos):
    visited.add(pos)
    x,y = pos
    val = steps[pos]
    for posn in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]:
        xn,yn = posn
        if ((xn >= 0 and xn < ncols) and
            (yn >= 0 and yn < nrows) and
            (posn not in corrupt)):
            if posn not in steps:
                steps[posn] = val+1
                explore(posn)
            elif val+1 < steps[posn]:
                steps[posn] = val+1
                explore(posn)
            if posn not in visited:
                explore(posn)

explore((0,0))
answer1 = steps[(ncols-1,nrows-1)]
print('Part 1:', answer1)
            
flag = True
count = nline
while flag:
    x,y = [int(n) for n in lines[count].split(',')]
    corrupt.add((x,y))
    steps = {(0,0):0}
    explore((0,0))
    if (ncols-1,nrows-1) not in steps:
        flag = False
    else:
        count += 1
        
print('Part 2:', lines[count])
