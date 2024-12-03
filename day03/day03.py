#! /usr/bin/env python3

import re

#filename = 'test1.txt'
#filename = 'test2.txt'
filename = 'input.txt'

flag = True

def mul(x,y):
    global flag
    if flag:
        return x*y
    else:
        return 0

def do():
    global flag
    flag = True
    return 0
    
def dont():
    global flag
    flag = False
    return 0
    
with open(filename, 'r') as fin:
    line = fin.read()

x = re.findall('mul\(\d+,\d+\)', line)
answer1 = 0
for i in x:
    answer1 += eval(i)
print('Part 1:', answer1)

x = re.findall('mul\(\d+,\d+\)|do\(\)|don\'t\(\)', line)
answer2 = 0
for s in x:
    s = s.replace("'","")
    answer2 += eval(s)
print('Part 2:', answer2)
