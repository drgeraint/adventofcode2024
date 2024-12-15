#! /usr/bin/env python3

#filename = 'test1.txt'
#filename = 'test2.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

Walls = dict()
Boxes = dict()
WideBoxes = dict()

class Wall:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        Walls[(row,col)] = self
        
class Box:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        Boxes[(row,col)] = self
    def push(self,dir):
        if dir == '^':
            nxt = (self.row-1,self.col)
        elif dir == 'v':
            nxt = (self.row+1,self.col)
        elif dir == '<':
            nxt = (self.row,self.col-1)
        elif dir == '>':
            nxt = (self.row,self.col+1)
        if nxt in Walls:
            return False
        if nxt in Boxes:
            if not Boxes[nxt].push(dir):
                return False
        if nxt in WideBoxes:
            if not WideBoxes[nxt].push(dir):
                return False
        self.move(nxt)
        return True
    def move(self,nxt):
        del Boxes[self.row,self.col]
        self.row,self.col = nxt
        Boxes[self.row,self.col] = self

class WideBox:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        WideBoxes[(row,col)] = self
    def test(self,dir):
        r,c = self.row,self.col
        if dir == '^':
            if (r-1,c) in Walls or (r-1,c+1) in Walls:
                return False
            for pos in [(r-1,c-1),(r-1,c),(r-1,c+1)]:
                if pos in WideBoxes:
                    if not WideBoxes[pos].test(dir):
                        return False
            return True
        elif dir == 'v':
            if (r+1,c) in Walls or (r+1,c+1) in Walls:
                return False
            for pos in [(r+1,c-1),(r+1,c),(r+1,c+1)]:
                if pos in WideBoxes:
                    if not WideBoxes[pos].test(dir):
                        return False
            return True
        elif dir == '<':
            if (r,c-1) in Walls:
                return False
            if (r,c-2) in WideBoxes:
                if not WideBoxes[(r,c-2)].test(dir):
                    return False
            return True
        elif dir == '>':
            if (r,c+2) in Walls:
                return False
            if (r,c+2) in WideBoxes:
                if not WideBoxes[(r,c+2)].test(dir):
                    return False
            return True        
    def push(self,dir):
        if not self.test(dir):
            return False
        r,c = self.row,self.col
        if dir == '^':
            for pos in [(r-1,c-1),(r-1,c),(r-1,c+1)]:
                if pos in WideBoxes:
                    WideBoxes[pos].push(dir)
                nxt = (r-1,c)
        elif dir == 'v':
            for pos in [(r+1,c-1),(r+1,c),(r+1,c+1)]:
                if pos in WideBoxes:
                    WideBoxes[pos].push(dir)
                nxt = (r+1,c)
        elif dir == '<':
            if (r,c-2) in WideBoxes:
                WideBoxes[(r,c-2)].push(dir)
            nxt = (r,c-1)
        elif dir == '>':
            if (r,c+2) in WideBoxes:
                WideBoxes[(r,c+2)].push(dir)
            nxt = (r,c+1)
        self.move(nxt)
        return True
    def move(self,nxt):
        del WideBoxes[self.row,self.col]
        self.row,self.col = nxt
        WideBoxes[self.row,self.col] = self
                
class Robot:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    def move(self,dir):
        r,c = self.row,self.col
        if dir == '^':
            if (r-1,c) in Walls:
                return False
            if (r-1,c) in Boxes:
                if not Boxes[(r-1,c)].push(dir):
                    return False
            for pos in [(r-1,c-1),(r-1,c)]:
                if pos in WideBoxes:
                    if not WideBoxes[pos].push(dir):
                        return False
            self.row -= 1
            return True
        elif dir == 'v':
            if (r+1,c) in Walls:
                return False
            if (r+1,c) in Boxes:
                if not Boxes[(r+1,c)].push(dir):
                    return False
            for pos in [(r+1,c-1),(r+1,c)]:
                if pos in WideBoxes:
                    if not WideBoxes[pos].push(dir):
                        return False
            self.row += 1
            return True
        elif dir == '<':
            if (r,c-1) in Walls:
                return False
            if (r,c-1) in Boxes:
                if not Boxes[(r,c-1)].push(dir):
                    return False
            if (r,c-2) in WideBoxes:
                if not WideBoxes[(r,c-2)].push(dir):
                    return False
            self.col -= 1
            return True
        elif dir == '>':
            if (r,c+1) in Walls:
                return False
            if (r,c+1) in Boxes:
                if not Boxes[(r,c+1)].push(dir):
                    return False
            if (r,c+1) in WideBoxes:
                if not WideBoxes[(r,c+1)].push(dir):
                    return False
            self.col += 1
            return True
    
phase=1
row = 0
for line in lines:
    if len(line) == 0:
        phase = 2
        cmd = []
    elif phase == 1:
        for col in range(0,len(line)):
            if line[col] == '#':
                Wall(row,col)
            elif line[col] == 'O':
                Box(row,col)
            elif line[col] == '@':
                R = Robot(row,col)
            else:
                assert(line[col] == '.')
        row += 1
    else:
        cmd.append(line)
        
nrows = row
ncols = len(lines[0])

def display():
    grid = []
    line = ['.']*ncols
    for row in range(0,nrows):
        grid.append(line.copy())
    row,col = 0,0
    for row,col in Walls:
        grid[row][col] = '#'
    for row,col in Boxes:
        grid[row][col] = 'O'
    grid[R.row][R.col] = '@'
    for line in grid:
        s = ''.join([x for x in line])
        print(s)

def displayWide():
    grid = []
    line = ['.']*ncols
    for row in range(0,nrows):
        grid.append(line.copy())
    row,col = 0,0
    for row,col in Walls:
        grid[row][col] = '#'
    for row,col in WideBoxes:
        grid[row][col]   = '['
        grid[row][col+1] = ']'
    grid[R.row][R.col] = '@'
    for line in grid:
        s = ''.join([x for x in line])
        print(s)
        
#display()
for line in cmd:
    for c in line:
        R.move(c)
        #display()

answer1 = 0
for row,col in Boxes:
    answer1 += 100*row + col
print('Part 1:', answer1)

############ PART 2 ############

with open(filename, 'r') as f:
    lines = f.read().splitlines()

Boxes     = dict()
Walls     = dict()
WideBoxes = dict()

phase=1
row = 0
for line in lines:
    if len(line) == 0:
        phase = 2
        cmd = []
    elif phase == 1:
        line = line.replace('#','##')
        line = line.replace('.','..')
        line = line.replace('O','[]')
        line = line.replace('@','@.')
        ncols = len(line)
        for col in range(0,ncols):
            if line[col] == '#':
                Wall(row,col)
            elif line[col] == '[':
                WideBox(row,col)
            elif line[col] == ']':
                assert((row,col-1) in WideBoxes)
            elif line[col] == '@':
                R = Robot(row,col)
            else:
                assert(line[col] == '.')
        row += 1
    else:
        cmd.append(line)
        
#displayWide()
for line in cmd:
    for c in line:
        R.move(c)
#displayWide()

answer2 = 0
for row,col in WideBoxes:
    answer2 += 100*row+col
print('Part 2:',answer2)
                
