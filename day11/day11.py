#! /usr/bin/env python3

import functools

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()
line = lines[0].split(' ')
    
@functools.cache
def process(x, blink, blinks):
    blink = blink+1
    n = len(x)
    if int(x) == 0:
        y = ['1']
    elif int(n/2) == n/2:
        y = [str(int(x[:int(n/2)])), str(int(x[int(n/2):]))]
    else:
        y = [str(int(x)*2024)]
    if blink == blinks:        
        z = len(y)
    else:
        z = 0
        for x in y:
            z += process(x,blink,blinks)
    return z

for p in [('1',25), ('2',75)]:
    answer = 0
    for x in line:
        answer += process(x,0,p[1])
    print('Part '+p[0]+':', answer)
