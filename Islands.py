"""
岛问题
一个矩阵汇总只有0和1两种值，每个位置都可以和自己的上下
左右四个位置相连，如果有一片1连在一起，这部分叫做一个岛
求一个矩阵总有多少个岛(单cpu下)
"""
"""
若将岛分为几部分进行求解
1.查询边界信息，若A,C所在集合是否为一个，若不为1个，合并，岛数减一
2.递归所有边界信息，查询集合是否属于一个，最终获得岛数
3.并行计算框架
"""
def countIslands(matrix):
    if matrix == None or matrix[0] == None:
        return 0
    N = len(matrix)
    M = len(matrix[0])
    res = 0
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1:
                res += 1
                infect(matrix, i, j, N, M)
    return res

def infect(matrix, i, j, N, M):
    if (i < 0 or i >= N or j < 0 or j>=M or
     matrix[i][j] != 1):
        return
    matrix[i][j] = 2
    infect(matrix, i+1, j, N, M)
    infect(matrix, i-1, j, N, M)
    infect(matrix, i, j+1, N, M)
    infect(matrix, i, j-1, N, M)

if __name__ == "__main__":
    matrix1 = [  [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
				        [ 0, 1, 1, 1, 0, 1, 1, 1, 0 ], 
				        [ 0, 1, 1, 1, 0, 0, 0, 1, 0 ],
				        [ 0, 1, 1, 0, 0, 0, 0, 0, 0 ], 
				        [ 0, 0, 0, 0, 0, 1, 1, 0, 0 ], 
				        [ 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
				        [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], ]
    print(countIslands(matrix1))
    matrix2 = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], 
						[ 0, 1, 1, 1, 1, 1, 1, 1, 0 ], 
						[ 0, 1, 1, 1, 0, 0, 0, 1, 0 ],
						[ 0, 1, 1, 0, 0, 0, 1, 1, 0 ], 
						[ 0, 0, 0, 0, 0, 1, 1, 0, 0 ], 
						[ 0, 0, 0, 0, 1, 1, 1, 0, 0 ],
						[ 0, 0, 0, 0, 0, 0, 0, 0, 0 ], ]
    print(countIslands(matrix2))
