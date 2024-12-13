#! /usr/bin/env python3

import numpy as np

#filename = 'test1.txt'
filename = 'input.txt'

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
            #L = np.array([[l11,l12],[l21,l22]])
            #R = np.array([r1,r2])
            games.append((L,R))

wins = []
for game in games:
    L,R = game
    maxA = min([99,
                int((R[0]+1)/L[0][0]),
                int((R[1]+1)/L[1][0])])+1
    maxB = min([99,
                int((R[0]+1)/L[0][1]),
                int((R[1]+1)/L[1][1])])+1
    minA = max([1,
                int(np.mod(R[0],L[0][1])/L[0][0]),
                int(np.mod(R[1],L[1][1])/L[1][0])])-1
    minB = max([1,
                int(np.mod(R[0],L[0][0])/L[0][1]),
                int(np.mod(R[1],L[1][0])/L[1][1])])-1
    best = ()
    cost = 3*R[0]+R[1]
    minA,maxA = 0,100
    for A in range(minA,maxA):
        B = int((R[0]-L[0][0]*A)/L[0][1])
        b = (R[1]-L[1][0]*A)/L[1][1]
        #print(A,b1,b2)
        if B == b:
            J = 3*A+B
            if J < cost:
                cost = J
                best = (A,B)
    if best != ():
        wins.append(cost)

print('Part 1:', sum(wins))
            
