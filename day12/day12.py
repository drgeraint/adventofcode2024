#! /usr/bin/env python3

#filename = 'test1.txt'
#filename = 'test2.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

nrows = len(lines)
ncols = len(lines[0])
    
allocated = set()
    
class Region:

    def __init__(self, pos):
        r,c = pos        
        self.plant = lines[r][c]
        self.plots = set()
        self.edges = { 't': set(),
                       'b': set(),
                       'l': set(),
                       'r': set() }
        self.add(pos)
        
    def add(self, pos):
        self.plots.add(pos)
        allocated.add(pos)
        r,c = pos
        for p in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
            if p not in allocated:
                x,y = p
                if (x >= 0 and x < nrows and
                    y >= 0 and y < ncols):
                    if lines[x][y] == self.plant:
                        self.add((x,y))

    def len(self):
        return len(self.plots)

    def area(self):
        area = 0
        for pos in self.plots:
            r,c = pos
            for p in [(r-1,c),(r+1,c),(r,c-1),(r,c+1)]:
                if p not in self.plots:
                    area += 1
        return area

    def sides(self):
        for pos in self.plots:
            r,c = pos
            if (r-1,c) not in self.plots:
                self.edges['t'].add(pos)
            if (r+1,c) not in self.plots:
                self.edges['b'].add(pos)
            if (r,c-1) not in self.plots:
                self.edges['l'].add(pos)
            if (r,c+1) not in self.plots:
                self.edges['r'].add(pos)
        for e in ['t','b']:
            removal = set()
            for pos in self.edges[e]:
                r,c = pos
                if (r,c-1) in self.edges[e]:
                    removal.add(pos)
            for pos in removal:
                self.edges[e].remove(pos)
        for e in ['l','r']:
            removal = set()
            for pos in self.edges[e]:
                r,c = pos
                if (r+1,c) in self.edges[e]:
                    removal.add(pos)
            for pos in removal:
                self.edges[e].remove(pos)
        sides = 0
        for e in ['t','b','l','r']:
            sides += len(self.edges[e])
        return sides
            
    def cost1(self):
        return self.len()*self.area()
    
    def cost2(self):
        return self.len()*self.sides()
    
    def print(self):
        print('Region ('+self.plant+'):', self.plots)
        print('Length:', self.len())
        print('Area:', self.area())
        print('Cost:', self.cost())
        
regions = set()
for row in range(0,nrows):
    for col in range(0,ncols):
        if (row,col) not in allocated:
            regions.add(Region((row,col)))

cost1 = 0
for region in regions:
    cost1 += region.cost1()
print('Part 1:', cost1)

cost2 = 0
for region in regions:
    cost2 += region.cost2()
print('Part 2:', cost2)
