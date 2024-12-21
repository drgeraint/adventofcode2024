#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

towels = []
for towel in lines[0].split(', '):
    towels.append(towel)
towels.sort()
    
patterns = []
for line in lines[2:]:
    patterns.append(line)

def find_overlap(string,substring):
    flag = True
    count = 0
    l = set()
    while flag:
        if substring in string:
            i = string.index(substring)
            j = i+len(substring)
            for k in range(i,j):
                l.add(k+count)
            count += i+1
            string = string[i+1:]
        else:
            flag = False
    return l
    
answer1 = 0
substrings = dict()
for pattern in patterns:
    characters = set()
    for x in range(0,len(pattern)):
        characters.add(x)
    substrings[pattern] = set()
    for towel in towels:
        if towel in pattern:
            for x in find_overlap(pattern,towel):
                substrings[pattern].add(x)
    if substrings[pattern] == characters:
        answer1 += 1

print('Part 1:', answer1)

