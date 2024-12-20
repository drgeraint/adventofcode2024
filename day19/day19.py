#! /usr/bin/env python3

import numpy as np
import re

filename = 'test1.txt'
#filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

towels = []
for towel in lines[0].split(', '):
    towels.append(towel)

patterns = []
for line in lines[2:]:
    patterns.append(line)

answer1 = 0
substrings = dict()
for pattern in patterns:
    characters = set()
    for x in range(0,len(pattern)):
        characters.add(x)
    substrings[pattern] = set()
    for towel in towels:
        if towel in pattern:
            for s in re.finditer(towel,pattern):
                x = s.span()
                for y in range(x[0],x[1]):
                    substrings[pattern].add(y)
    if substrings[pattern] == characters:
        answer1 += 1
print('Part 1:', answer1)
