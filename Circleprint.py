"""
给定一个整型矩阵matrix，按照圆圈的方式打印它
额外空间复杂度为O(1)
"""

class Circleprint:
    def __init__(self, matrix):
        self.matrix = matrix
        self.tr = 0
        self.tc = 0
        self.dr = len(matrix) - 1
        self.dc = len(matrix[0]) - 1
    
    def orderprint(self):
        while self.tr <= self.dr and self.tc <= self.dc:
            self.printEdge()
            self.tr += 1
            self.tc += 1
            self.dr -= 1
            self.dc -= 1
    
    def printEdge(self):
        if self.tr == self.dr:
            for i in range(self.tc, self.dc+1):
                print(self.matrix[self.tr][i])
        elif self.tc == self.dc:
            for i in range(self.tr, self.dr+1):
                print(self.matrix[i][self.tc])
        else:
            curc = self.tc
            curr = self.tr
            while curc != self.dc:
                print(self.matrix[self.tr][curc])
                curc += 1
            while curr != self.dr:
                print(self.matrix[curr][self.dc])
                curr += 1
            while curc != self.tc:
                print(self.matrix[self.dr][curc])
                curc -= 1
            while curr != self.tr:
                print(self.matrix[curr][self.tc])
                curr -= 1

if __name__ == "__main__":
    import numpy as np
    matrix = np.arange(1, 13).reshape(3,4)
    print(matrix)
    printcircle = Circleprint(matrix)
    printcircle.orderprint()
            