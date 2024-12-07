#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

def eval_list(lhs,rhs):
    mul = [rhs[0]*rhs[1]]
    add = [rhs[0]+rhs[1]]
    if len(rhs) == 2:
        return lhs == mul[0] or lhs == add[0]
    else:
        mul.extend(rhs[2:])
        add.extend(rhs[2:])
        return eval_list(lhs, mul) or eval_list(lhs, add)

count = 0
    
for line in lines:
    lhs, rhs = line.split(': ')
    lhs = int(lhs)
    rhs = rhs.split(' ')
    rhs = [int(x) for x in rhs]
    if eval_list(lhs, rhs):
        count += lhs
print('Part 1:', count)
    
                           
