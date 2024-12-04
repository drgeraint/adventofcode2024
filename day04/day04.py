#! /usr/bin/env python3

import re

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrow = len(lines)
ncol = len(lines[0])

count = 0
E  = lines.copy()
S  = list()
SE = list()
NE = list()

for j in range(0, ncol):
    s = ''
    for i in range(0, nrow):
        s += lines[i][j]
    S.append(s)

for j in range(0, ncol):
    se = ''
    for k in range(0, ncol-j):
        se += lines[k][j+k]
    SE.append(se)
    ne = ''
    for k in range(0, j+1):
        ne += lines[j-k][k]
    NE.append(ne)
    ne = ''

for j in range(0, ncol-1):
    ne = ''
    for k in range(1, ncol-j):
        ne += lines[ncol-k][j+k]
    NE.append(ne)
        
for i in range(1, nrow):
    se = ''
    for k in range(0, nrow-i):
        se += lines[i+k][k]
    SE.append(se)

    
# print(lines)
# print(len(S))
# print(len(SE))
# print(len(NE))
E.extend(S)
E.extend(SE)
E.extend(NE)

c = list()
for e in E:
    c.extend(re.findall('XMAS', e))
    c.extend(re.findall('SAMX', e))

print('Part 1:', len(c))

count = 0
for i in range(1, nrow-1):
    for j in range(1, ncol-1):
        if lines[i][j] == 'A':
            if ((((lines[i-1][j-1] == 'M') and
                 (lines[i+1][j+1] == 'S')) or
                ((lines[i-1][j-1] == 'S') and
                 (lines[i+1][j+1] == 'M'))) and
                (((lines[i-1][j+1] == 'M') and
                  (lines[i+1][j-1] == 'S')) or
                 ((lines[i-1][j+1] == 'S') and
                  (lines[i+1][j-1] == 'M')))):
                count += 1
print('Part 2:', count)
                        
