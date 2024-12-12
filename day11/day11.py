#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

memo = dict()
line = lines[0].split(' ')
for i in range(0,75):
    new_line = []
    for x in line:
        if x in memo:
            y = memo[x]
        else:
            n = len(x)
            if int(x) == 0:
                y = ['1']
            elif int(n/2) == n/2:
                y = [str(int(x[:int(n/2)])), str(int(x[int(n/2):]))]
            else:
                y = [str(int(x)*2024)]
            memo[x] = y
        new_line.extend(y)
        line = new_line
    if i == 25-1:
        print('Part 1:', len(line))
print('Part 2:', len(line))
