#! /usr/bin/env python3

import numpy as np
import scipy.optimize as opt

filename = 'test1.txt'
#filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

games = []
    
for line in lines:
    if line != '':
        label, data = line.split(': ')
        x1, x2 = [int(x[2:]) for x in data.split(', ')]    
        if label == 'Button A':
            l11, l21 = x1, x2
        elif label == 'Button B':
            l12, l22 = x1, x2
            L = ((l11,l12),(l21,l22))
        elif label == 'Prize':
            r1, r2 = x1, x2
            R = (r1,r2)
            games.append((L,R))

wins = []
for game in games:
    L,R = game
    best = ()
    cost = 3*R[0]+R[1]
    for A in range(0,100):
        B = int((R[0]-L[0][0]*A)/L[0][1])
        b = (R[1]-L[1][0]*A)/L[1][1]
        if B == b:
            J = 3*A+B
            if J < cost:
                cost = J
                best = (A,B)
    if best != ():
        wins.append(cost)

print('Part 1:', sum(wins))

gain = 10000000000000
cost = 0
for game in games:
    L,R = game
    A = np.array([[L[0][0],L[0][1]],[L[1][0],L[1][1]]])
    B = np.array([R[0],R[1]])*gain
    C = np.array([3,1])
    constraints = opt.LinearConstraint(A, B, B)
    integrality = np.ones_like(C)
    res = opt.milp(c=C, constraints=constraints, integrality=integrality)
    print(res.x)
    if res.x is not None:
        cost += int(sum(C*res.x))

print('Part 2:', cost)


# Wrong answer: 321046574547349952 is too high
