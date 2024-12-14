#! /usr/bin/env python3

import numpy as np
import re

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

if filename == 'test1.txt':
    ncols = 11
    nrows = 7
else:
    ncols = 101
    nrows = 103

robots = []
class Robot:
    def __init__(self,line):
        line = line.replace('=',' ')
        line = line.replace(',',' ')
        data = line.split(' ')
        self.p = (int(data[1]),int(data[2]))
        self.v = (int(data[4]),int(data[5]))
        robots.append(self)
        
    def move(self,dt):
        px,py = self.p
        vx,vy = self.v
        px = np.mod(px + vx*dt,ncols)
        py = np.mod(py + vy*dt,nrows)
        self.p = (px,py)

for line in lines:
    Robot(line)

for t in range(0,1):
    Q1,Q2,Q3,Q4 = 0,0,0,0
    for r in robots:
        r.move(100)
        x,y = r.p
        if x < int(ncols/2) and y < int(nrows/2):
            Q1 += 1
        elif x > int(ncols/2) and y < int(nrows/2):
            Q2 += 1
        elif x < int(ncols/2) and y > int(nrows/2):
            Q3 += 1
        elif x > int(ncols/2) and y > int(nrows/2):
            Q4 += 1

answer1 = Q1*Q2*Q3*Q4
print('Part 1:', answer1)
