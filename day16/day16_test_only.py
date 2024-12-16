#! /usr/bin/env python3

import functools

filename = 'test2.txt'
#filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

blocks = set()
spaces = set()

for row in range(0,ncols):
    for col in range(0,nrows):
        c = lines[row][col]
        if c == 'S':
            start = (row,col)
        elif c == 'E':
            end = (row,col)
        elif c == '#':
            blocks.add((row,col))
        elif c == '.':
            spaces.add((row,col))

def reduce_blocks():
    flag = True
    while flag:
        flag = False
        record = set()
        for r,c in spaces:
            count = 0
            for pos in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if pos in blocks:
                    count += 1
            if count > 2:
                blocks.add((r,c))
                record.add((r,c))
                flag = True
        for pos in record:
            spaces.remove(pos)

def display():
    for row in range(0,nrows):
        line = ''
        for col in range(0,ncols):
            if start == (row,col):
                c = 'S'
            elif end == (row,col):
                c = 'E'
            elif (row,col) in blocks:
                c = '#'
            elif (row,col) in spaces:
                c = '.'
            else:
                error('Undefined block:',row,col)
            line = line+c            
        print(line)

def display_path(path):
    for row in range(0,nrows):
        line = ''
        for col in range(0,ncols):
            if start == (row,col):
                c = 'S'
            elif end == (row,col):
                c = 'E'
            elif (row,col) in blocks:
                c = '#'
            elif (row,col) in spaces:
                if (row,col) in path:
                    c = '.'
                else:
                    c = ' '
            else:
                error('Undefined block:',row,col)
            line = line+c            
        print(line)



@functools.cache        
def cost_pair(pos0,pos1,direction):
    r0,c0 = pos0
    r1,c1 = pos1
    if (r1 == r0 and
        c1 == c0+1):
        new_direction = 'E'
    elif (r1 == r0 and
          c1 == c0-1):
        new_direction = 'W'
    elif (r1 == r0-1 and
          c1 == c0):
        new_direction = 'N'
    elif (r1 == r0+1 and
          c1 == c0):
        new_direction = 'S'
    if direction == new_direction:
        cost = 1
    else:
        cost = 1001
    return (cost,new_direction)

def cost_route(route):
    cost = 0
    direction = 'E'
    for i in range(1,len(route)):
        pair_cost,direction = cost_pair(route[i-1],route[i],direction)
        cost += pair_cost
    return cost

reduce_blocks()
display()
print('Reduced blocks')

routes = []
paths = []
path = [start]
paths.append(path)
    
while len(paths) > 0:
    for path in paths:
        r,c = path[-1]
        for pos in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            new_path = path.copy()
            new_path.append((pos))
            if pos == end:
                routes.append(new_path)
            elif pos not in path and pos in spaces:
                paths.append(new_path)
        paths.remove(path)
        
J = None
for route in routes:
    cost = cost_route(route)
    if not J or cost < J:
        display_path(route)
        J = cost
        print('J:',J)
print('Part 1:',J)
