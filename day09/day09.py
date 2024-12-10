#! /usr/bin/env python3

import re

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()
line = lines[0]
    
s     = []
free  = []
names = []
posn  = 0
for i in range(0,len(line)):
    if int(i/2) == i/2:
        c = int(i/2)
        names.append(c)
    else:
        c = ''
        free.append((posn,int(line[i])))
    for j in range(0,int(line[i])):
        s.append(c)
    posn += int(line[i])
t = s.copy()                    # save for part 2
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

free.sort()
free_spans = list()             # (span, posn)

while names:
    name = names.pop()
    span = t.count(name)
    posn = t.index(name)
    f = [x for x in free if x[1]>=span]
    if len(f) > 0 and f[0][0] < posn:        
        old_posn = posn
        new_posn = f[0][0]
        for k in range(0,span):
            t[new_posn+k] = name
            t[old_posn+k] = ''
        free.append((old_posn,span))
        free.remove(f[0])
        if f[0][1] > span:
            free.append((new_posn+span,f[0][1]-span))
        free.sort()
        while s[-1] == '':
            s.pop()

answer2 = 0
for i in range(0,len(t)):
    if t[i] == '':
        t[i] = 0
    answer2 += i*t[i]
print('Part 2:', answer2)
