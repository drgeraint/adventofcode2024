#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

games = []
    
for line in lines:
    if line != '':
        label, data = line.split(': ')
        x,y = [int(i[2:]) for i in data.split(', ')]    
        if label == 'Button A':
            l11,l21 = x,y
        elif label == 'Button B':
            l12,l22 = x,y
            L = ((l11,l12),(l21,l22))
        elif label == 'Prize':
            r1,r2 = x,y
            R = (r1,r2)
            games.append((L,R))

def eval_games(offset):
    cost = 0
    for game in games:
        L,R = game
        R = (R[0]+offset,R[1]+offset)
        Adj = ((L[1][1],-L[0][1]),(-L[1][0],L[0][0]))
        Det = L[0][0]*L[1][1]-L[0][1]*L[1][0]
        A = Adj[0][0]*R[0]+Adj[0][1]*R[1]
        B = Adj[1][0]*R[0]+Adj[1][1]*R[1]
        A /= Det
        B /= Det
        if A == int(A) and B == int(B):
            cost += int(3*A+B)
    return cost
            
print('Part 1:', eval_games(0))        

offset = 10000000000000
print('Part 2:', eval_games(offset))
