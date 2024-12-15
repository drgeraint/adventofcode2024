#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

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

def part1(dt):
    Q1,Q2,Q3,Q4 = 0,0,0,0
    for r in robots:
        r.move(dt)
        x,y = r.p
        if x < int(ncols/2) and y < int(nrows/2):
            Q1 += 1
        elif x > int(ncols/2) and y < int(nrows/2):
            Q2 += 1
        elif x < int(ncols/2) and y > int(nrows/2):
            Q3 += 1
        elif x > int(ncols/2) and y > int(nrows/2):
            Q4 += 1
    return (Q1,Q2,Q3,Q4)

Q = part1(100)
print('Part 1:', np.product(Q))

def plot(t):
    grid = []
    line = [' ']*ncols
    for r in range(0,nrows):
        grid.append(line.copy())
    for robot in robots:
        col,row = robot.p
        grid[row][col] = '*'
    for line in grid:
        s = ''.join([c for c in line])
        print(s)
    print('Time:', t)

def evalQ(Q):
    X,Y = [],[]
    for r in robots:
        x,y = r.p
        X.append(x)
        Y.append(y)
    J = (np.var(X),np.var(Y))
    return J
         
# View tree without looping for my input
robots = []
for line in lines:
   Robot(line)
part1(8159)
plot(8159)

# Finding min var(x) and var(y) will work for other inputs
data = {'Jx':[], 'Jy':[]}
robots = []
for line in lines:
    Robot(line)
for move in range(0,nrows*ncols):
    Q = part1(1)
    J = evalQ(Q)
    Jx,Jy = J
    data['Jx'].append(Jx)
    data['Jy'].append(Jy)
    if Jx < 400 and Jy < 400:
        tree = move
        plot(tree)
print('Part 2:', tree+1)

plt.plot(data['Jx'],data['Jy'],'.')
plt.title('var(y) against var(x)')
plt.show()
              
