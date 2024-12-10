#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

grid  = dict()
zeros = set()
nines = set()
trail = dict()

def follow(start,pos):
    val = grid[pos]
    if val == 9:
        trail[start].add(pos)
    else:
        r = pos[0]
        c = pos[1]
        for nxt in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if (nxt[0] >= 0 and nxt[0] < nrows and
                nxt[1] >= 0 and nxt[1] < ncols):
                if grid[nxt] == val+1:
                    follow(start,nxt)
                
                
for row in range(0,nrows):
    for col in range(0,ncols):
        c = int(lines[row][col])
        grid[(row,col)] = c
        if c == 0:
            zeros.add((row,col))
            trail[(row,col)] = set()
        elif c == 9:
            nines.add((row,col))
                  
for z in zeros:
    follow(z,z)

answer1 = 0
for z in trail:
    answer1 += len(trail[z])
print(answer1)

