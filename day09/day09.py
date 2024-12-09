#! /usr/bin/env python3

import re

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()
line = lines[0]
    
s = []
for i in range(0,len(line)):
    if int(i/2) == i/2:
        c = int(i/2)
    else:
        c = ''
    for j in range(0,int(line[i])):
        s .append(c)
r = s.copy()
r = [x for x in r if x != '']

while '' in s:
    i = s.index('')
    s[i] = r.pop()
    while s[-1] == '':
        s.pop()
    s.pop()

answer1 = 0
for i in range(0,len(s)):
    answer1 += i*s[i]
print('Part 1:', answer1)

