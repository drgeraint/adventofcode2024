#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as fin:
    lines = fin.read().splitlines()

def sub(a,b):
    return int(a)-int(b)

def check_safe(report):
    dif = list(map(sub, report[:-1], report[1:]))
    safe_p = (+1,+2,+3)
    safe_n = (-1,-2,-3)
    if dif[0] in safe_p:
        safe = safe_p
    elif dif[0] in safe_n:
        safe = safe_n
    else:
        return 0
    for i,x in enumerate(dif):
        if x not in safe:
            unsafe = True
            return 0
    return 1

def check_safe_damped(report):
    dif = list(map(sub, report[:-1], report[1:]))
    safe_p = (+1,+2,+3)
    safe_n = (-1,-2,-3)
    if dif[0] in safe_p:
        safe = safe_p
    elif dif[0] in safe_n:
        safe = safe_n
    else:
        report0 = report[1:]
        report1 = report.copy()
        del(report1[1])
        return check_safe(report0) or check_safe(report1)
    for i,x in enumerate(dif):
        if x not in safe:
            report0 = report.copy()
            del(report0[i-1])
            report1 = report.copy()
            del(report1[i])
            report2 = report.copy()
            del(report2[i+1])
            return (check_safe(report0) or
                    check_safe(report1) or
                    check_safe(report2))
    return 1

answer1 = 0
answer2 = 0
for line in lines:
    report = line.split(' ')
    answer1 += check_safe(report)
    answer2 += check_safe_damped(report)
print('Part 1:', answer1)
print('Part 2:', answer2)
        
