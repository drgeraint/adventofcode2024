#! /usr/bin/env python3

import sys
sys.setrecursionlimit(100000000)

#filename = 'test2.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])

blocks = set()
spaces = set()
visited = set()
costs  = dict()

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

def rotation_cost(direction0,direction1):
    if direction0 == direction1:
        cost = 0
    elif (direction0 == 'N' and direction1 == 'S' or
          direction0 == 'E' and direction1 == 'W' or
          direction0 == 'W' and direction1 == 'E' or
          direction0 == 'S' and direction1 == 'N'):
        cost = 2000
    else:
        cost = 1000
    return cost

def update_node_costs(node,direction,val):
    if node not in costs:
        costs[node] = {direction:val}
    for d in ['N','E','W','S']:
        dcost = val + rotation_cost(direction,d)
        if d not in costs[node]:
            costs[node][d] = dcost
        else:
            if dcost < costs[node][d]:
                costs[node][d] = dcost
                traverse(node,direction)
    #if len(costs.keys()) < 20:
        #print(node, costs[node])
                
def traverse(node,last_direction):
    visited.add(node)
    r,c = node
    N = (r-1,c)
    E = (r,c+1)
    S = (r+1,c)
    W = (r,c-1)
    for nxt,direction in [((r-1,c),'N'),
                          ((r,c+1),'E'),
                          ((r+1,c),'S'),
                          ((r,c-1),'W')]:
        if nxt in spaces or nxt == end:
            cost = costs[node][direction] + 1
            update_node_costs(nxt,direction,cost)
            if nxt not in visited:
                traverse(nxt,direction)
            
reduce_blocks()
display()
update_node_costs(start,'E',0)
traverse(start,'E')
answer1 = min(costs[end].values())
print('Part 1:', answer1)
print(costs[end])
