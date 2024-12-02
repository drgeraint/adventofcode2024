#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

list_a = []
list_b = []
for line in lines:
    a,b = line.split()
    a = int(a)
    b = int(b)
    list_a.append(a)
    list_b.append(b)
list_a.sort()
list_b.sort()
answer1 = 0
for i, x in enumerate(list_a):
    answer1 += abs(x-list_b[i])
print('part 1:', answer1)

answer2 = 0
for i, x in enumerate(list_a):
    answer2 += x*list_b.count(x)
print('part 2:', answer2)
