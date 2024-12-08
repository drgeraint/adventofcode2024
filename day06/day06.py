#! /usr/bin/env python3

import re

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrow = len(lines)
ncol = len(lines[0])

obstacles = set()
positions = set()

move = None

def up(pos):
    global move
    if pos[0] == 0:
        return None
    nxt = (pos[0]-1,pos[1])
    if nxt in obstacles:
        move = right
    else:
        pos = nxt
    return pos

def right(pos):
    global move
    if pos[1] == ncol-1:
        return None
    nxt = (pos[0],pos[1]+1)
    if nxt in obstacles:
        move = down
    else:
        pos = nxt
    return pos
    
def down(pos):
    global move
    if pos[0] == nrow-1:
        return None
    nxt = (pos[0]+1,pos[1])
    if nxt in obstacles:
        move = left
    else:
        pos = nxt
    return pos
    
def left(pos):
    global move
    if pos[1] == 0:
        return None
    nxt = (pos[0],pos[1]-1)
    if nxt in obstacles:
        move = up
    else:
        pos = nxt
    return pos

row = 0
for line in lines:
    for col in [x.span()[0] for x in re.finditer('#', line)]:
        obstacles.add((row,col))
    s = re.search('[v^<>]', line)
    if s:
        c = s.span()[0]
        start = (row,c)
        if line[c] == 'V':
            start_move = down
        elif line[c] == '^':
            start_move = up
        elif line[c] == '<':
            start_move = left
        elif line[c] == '>':
            start_move = right
    row += 1

pos = start
move = start_move
while pos:
    positions.add(pos)
    pos = move(pos)
print('Part 1:', len(positions))

count = 0
for row in range(0,nrow):
    for col in range(0,ncol):
        if (row,col) not in obstacles:
            positions = set()
            pos = start
            move = start_move
            obstacles.add((row,col))
            stop = False
            while pos and not stop:
                positions.add((pos,move))
                pos = move(pos)
                if (pos,move) in positions:
                    count += 1
                    stop = True
            obstacles.remove((row,col))
print('Part 2:', count)
