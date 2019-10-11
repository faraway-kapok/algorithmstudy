"""
求n!
汉诺塔问题
"""

#N： 1~N
#
def process(N, from_, to_, help_):
    if N == 1:
        print('Move 1 from ' + from_ + ' to ' + to_)
    else:
        process(N-1, from_, help_, to_)
        print('Move ' + str(N) + ' from ' + from_ + ' to ' + to_)
        process(N-1, help_, to_, from_)

# process(3, "左", "右", "中")

"""
打印一个字符串的全部子序列，包括空字符串
每个字符有两种状态，要或不要
"""
def printAllSub(arr, i, res):
    if i == len(arr):
        # print(res)
        return res
    printAllSub(arr, i+1, res)        #要
    printAllSub(arr, i+1, res+arr[i]) #不要

# arr = "abc"
# printAllSub(arr, 0, "")

"""
字符串的全排列
"""
def Permutation(arr):
    l = []
    if len(arr) <= 1:
        return arr
    n = len(arr)
    for i in range(n):
        for j in Permutation(arr[:i]+arr[i+1:]):
            temp = arr[i] + str(j)
            if temp not in l:
                l.append(temp)
    return l

# arr = "abc"
# printAllPermutations(arr, 0)
# print("===============================")


"""
母牛每年生一只母牛，新出生的母牛成长三年后，也能每年生出一只母牛，假设不会死。
求N年后，母牛的数量
F(n) = F(n-1) + F(n-3)
"""
def cowNumber(n):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
    return cowNumber(n-1) + cowNumber(n-3)

def cowNumber1(n):
    if n < 1:
        return 0
    if n == 1 or n == 2 or n == 3:
        return n
"""
二维数组中的每个数都是整数，要求从左上角走到右下角， 每一步只能向下或上向右
沿途经过的数字进行累加，返回最小的路径和
"""
#当前位置到右下角的最短路径和 递归
def walk(matrix, i, j):
    if i == len(matrix)-1 and j == len(matrix[0]) - 1:
        return matrix[i][j]
    if i == len(matrix) - 1:
        return matrix[i][j] + walk(matrix, i, j+1)
    if j == len(matrix[0]) - 1:
        return matrix[i][j] + walk(matrix, i+1, j)
    
    right = walk(matrix, i, j+1) #右边位置到右下角的最短路径和
    down = walk(matrix, i+1, j)  #下边位置到右下角的最短路径和
    return matrix[i][j] + min(right, down)

#动态规划
import numpy as np
def dpwalk(matrix, i, j):
    dp = np.zeros((len(matrix), len(matrix[0])))
    if i == len(matrix) - 1 and j == len(matrix[0]) - 1:
        dp[i][j] = matrix[i][j]
    if i == len(matrix) - 1:
        for j in reversed(range(len(matrix[0])-1)):
            dp[i][j] = matrix[i][j] + dp[i][j+1]
    if j == len(matrix[0]) - 1:
        for j in reversed(range(len(matrix)-1)):
            dp[i][j] = matrix[i][j] + dp[i+1][j]
    right = matrix[i][j] + dp[i][j+1]
    down = matrix[i][j] + dp[i+1][j]
    dp[i][j] = min(right, down)
        
matrix = [
    [1,3,5,9],
    [8,1,3,4],
    [5,0,6,1],
    [8,8,4,0],
]

print(walk(matrix, 0, 0))

"""
一个数组arr， 一个整数aim
如果可以任意选择arr中的数字，能不能累加得到aim，返回True或False
"""
def isSum(arr, i, res, aim):
    if i == len(arr):
        return res == aim
    return isSum(arr, i+1, res, aim) or isSum(arr, i+1, res+arr[i], aim)

arr = [1,4,8]
aim = 11
print(isSum(arr, 0, 0, aim))

