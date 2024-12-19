#! /usr/bin/env python3

import numpy as np

#filename = 'test1.txt'
filename = 'input.txt'

with open(filename, 'r') as f:
    lines = f.read().splitlines()

class Computer:
    def __init__(self):
        self.A,self.B,self.C = 0,0,0
        self.reset()
        
    def combo(self,operand):
        if operand < 4:
            return int(operand)
        elif operand == 4:
            return self.A
        elif operand == 5:
            return self.B
        elif operand == 6:
            return self.C
        else:
            error('Unexpected operand')

    def dv(self,operand):
        return int(self.A/pow(2,self.combo(operand)))
            
    def do(self,opcode,operand):
        if opcode == 0:
            self.A = self.dv(operand)
        elif opcode == 1:
            self.B = int(operand)^self.B
        elif opcode == 2:
            self.B = np.mod(self.combo(operand),8)
        elif opcode == 3:
            if self.A != 0:
                self.P = int(operand)-2
        elif opcode == 4:
            self.B = self.B^self.C
        elif opcode == 5:
            s = str(np.mod(self.combo(operand),8))
            if len(self.out) == 0:
                self.out = s
            else:
                self.out = self.out+','+s
        elif opcode == 6:
            self.B = self.dv(operand)
        elif opcode == 7:
            self.C = self.dv(operand)

    def reset(self):
        self.P = 0
        self.out = ''

    def compute(self):
        ops = [int(x) for x in self.program.split(',')]
        while self.P < len(ops):
            self.do(ops[self.P],ops[self.P+1])
            self.P += 2
        print('A:',self.A,'\tB:',self.B,'\tC:',self.C,
              '\tout:', self.out)

    def read(self,lines):
        for line in lines:
            if len(line) > 0:
                lhs,rhs = line.split(': ')
            if lhs == 'Register A':
                self.A = int(rhs)
            elif lhs == 'Register B':
                self.B = int(rhs)
            elif lhs == 'Register C':
                self.C = int(rhs)
            elif lhs == 'Program':
                self.reset()
                self.program = rhs

    def run(self,lines):
        self.read(lines)
        self.compute()
                
    def test(self):
        self.C = 9
        self.program = '2,6'
        self.reset()
        self.compute()

        self.A = 10
        self.program = '5,0,5,1,5,4'
        self.reset()
        self.compute()

        self.A = 2024
        self.program = '0,1,5,4,3,0'
        self.reset()
        self.compute()

        self.B = 29
        self.program = '1,7'
        self.reset()
        self.compute()

        self.B = 2024
        self.C = 43690
        self.program = '4,0'
        self.reset()
        self.compute()

                
c = Computer()
c.test()
c.run(lines)
