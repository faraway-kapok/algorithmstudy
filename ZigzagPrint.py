"""
Z字打印矩阵
"""
class ZigzagPrint:
    def __init__(self, matrix):
        self.matrix = matrix
        self.ar = 0
        self.ac = 0
        self.br = 0
        self.bc = 0
        self.endr = len(self.matrix) - 1
        print(self.endr)
        self.endc = len(self.matrix[0]) - 1
        print(self.endc)
        self.fromup = False
        while self.ar != (self.endr+1):
            self.printlevel(self.ar, self.ac, self.br, self.bc, self.fromup)
            self.ar = (self.ar + 1) if self.ac == self.endc else self.ar
            self.ac = self.ac if self.ac == self.endc else (self.ac + 1)
            self.bc = (self.bc+1) if self.br == self.endr else self.bc            
            self.br = self.br if self.br == self.endr else (self.br + 1)
            self.fromup = not self.fromup
        print()
        
    def printlevel(self, ar, ac, br, bc, fromup):
        if fromup:
            
            # while self.ar <= self.br and self.ac >= self.bc:
            while ar != (br+1):
                print(self.matrix[ar][ac], end=" ")
                ar += 1
                ac -= 1
                
        else:
            
            # while self.br >= self.ar and self.bc <= self.ac:
            while br != (ar-1):
                print(self.matrix[br][bc], end=" ")
                br -= 1
                bc += 1
                
    
if __name__ == "__main__":
    import numpy as np
    matrix = np.arange(1, 13).reshape(3,4)
    print(matrix)
    test = ZigzagPrint(matrix)