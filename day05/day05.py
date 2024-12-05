#! /usr/bin/env python3

#filename = 'test1.txt'
filename = 'input.txt'
    
class Pagination:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.lines = f.read().splitlines()
        self.prereqs = dict()
        self.updates = []
        self.incorrect_updates = []
        self.read_lines()
        #print(self.prereqs)
        #print(self.updates)
        self.evaluate()
        self.fix_updates()
        
    def read_lines(self):
        for line in self.lines:
            if '|' in line:
                x,y = line.split('|')
                self.process_prereq(x,y)
            elif ',' in line:
                update = [int(x) for x in line.split(',')]
                self.updates.append(update)
                
    def process_prereq(self, x,y):
        x = int(x)
        y = int(y)
        if y not in self.prereqs:
            self.prereqs[y] = set()
        self.prereqs[y].add(x)
            
    def confirm_order(self, update):
        OK = True
        for j,y in enumerate(update):
            if y in self.prereqs:
                for x in update[j+1:]:
                    if x in self.prereqs[y]:
                        OK = False
                        if update not in self.incorrect_updates:
                            self.incorrect_updates.append(update)
                        #print('NOT OK:', y, update[j+1:])
                    #else:
                        #print('OK:', y, update[j+1:])
        return OK

    def evaluate(self):
        value = 0
        for update in self.updates:
            if self.confirm_order(update):
                #print(update)
                n = len(update)
                value += update[int(n/2)]
        print('Part 1:', value)

    def fix_updates(self):
        #print(self.prereqs)
        #print(self.incorrect_updates)
        for update in self.incorrect_updates:
            #print(update)
            flag = True
            while flag:
                for j,y in enumerate(update):
                    if y in self.prereqs:
                        for x in update[j+1:]:
                            if x in self.prereqs[y]:
                                update.remove(y)
                                update.append(y)
                if self.confirm_order(update):
                    flag = False
        #print(self.incorrect_updates)
        value = 0
        for update in self.incorrect_updates:
            n = len(update)
            value += update[int(n/2)]
        print('Part 2:', value)            

        
p = Pagination(filename)
