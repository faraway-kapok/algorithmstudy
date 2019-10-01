class Rotatematrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.tr = 0
        self.tc = 0
        self.dr = len(matrix) - 1
        self.dc = len(matrix[0]) - 1
        while self.tr <= self.dr and self.tc <= self.dc:
            self.rotateEdage()
            self.tr += 1
            self.tc += 1
            self.dr -= 1
            self.dc -= 1
        
    def rotateEdage(self):
        times = self.dc - self.tc
        tmp = 0
        for i in range(0, times):
            tmp = self.matrix[self.tr][self.tc+i]
            self.matrix[self.tr][self.tc+i] = self.matrix[self.dr-i][self.tc]
            self.matrix[self.dr-i][self.tc] = self.matrix[self.dr][self.dc-i]
            self.matrix[self.dr][self.dc-i] = self.matrix[self.tr+i][self.dc]
            self.matrix[self.tr+i][self.dc] = tmp

    def printmatrix(self):
        print(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(self.matrix[i][j],end=" ")


if __name__ == "__main__":
    import numpy as np
    matrix = np.arange(1, 17).reshape(4,4)
    print(matrix)
    x = Rotatematrix(matrix)
    x.rotateEdage()
    x.printmatrix()    