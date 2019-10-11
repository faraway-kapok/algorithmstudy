"""矩阵m的p次方求解"""
import numpy as np
def matrixPower(matrix, p):
    res = np.zeros([len(matrix), matrix.shape[1]])
    #创建单位矩阵res
    for i in range(len(res)):
        res[i][i] = 1
    tmp = matrix
    while p != 0:
        if p & 1 != 0:
            res = muliMatrix(res, tmp)
        tmp = muliMatrix(tmp, tmp)
        p >>= 1
    return res

def muliMatrix(m1, m2):
    res = np.zeros([len(m1), m2.shape[1]])
    for i in range(len(m1)):
        for j in range(m2.shape[1]):
            for k in range(len(m2)):
                res[i,j] += m1[i,k] * m2[k,j]

    return res

def f3(n):
    if n < 1:
        return 0
    if n == 1 or n == 2:
        return 1
    base = np.matrix([[1,1], [1,0]])
    res = matrixPower(base, n-2)
    return int(res[0][0] + res[1][0])

print(f3(5))