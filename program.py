"""
IPO
做项目的最大收益问题
1.costs, profits. W初始资金 K最多可做K个项目
思路：
创建node类型数据，包含cost 以及profit
1.按照cost的大小创建小根堆costMinHeap
2.根据W初始资金，从cost小根堆中弹出小于等于W的项目，
如果costMinHeap为空或者剩下的项目花费都大于W，停止弹出。
并按照profit的值创建大根堆profitMaxHeap
3.1若profitMaxHeap为空，表明当前W 未解锁任何项目，
其次说明已经没有任何项目可以挑选，直接返回W
3.2若profitMaxHeap不为空，弹出栈顶项目，
即为programbest，完成项目后将该项目的收益加到W上
4.重复步骤2，进行新一轮的解锁
5.如果步骤3进行的过程中没有返回，
那么做完K个项目后，返回W
"""
import heapq

class MinCostNode:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit
    
    def __lt__(self, other):
        return self.cost < other.cost

class MaxProfitNode:
    def __init__(self, cost, profit):
        self.cost = cost
        self.profit = profit
    
    def __lt__(self, other):
        return self.profit > other.profit

def findMaximizedCapital(k, w, profits, costs):

    costMinHeap = []
    profitMaxHeap = []
    for i in range(len(costs)):
        node = MinCostNode(costs[i], profits[i])
        heapq.heappush(costMinHeap, node)
    for i in range(k):
        while len(costMinHeap) != 0 and costMinHeap[0].cost <= w:
            node = heapq.heappop(costMinHeap)
            max_node = MaxProfitNode(node.cost, node.profit)
            heapq.heappush(profitMaxHeap, max_node)
        if len(profitMaxHeap) == 0:
            return w
        w += heapq.heappop(profitMaxHeap).profit
    return w
    


if __name__ == '__main__':
    costs = [5, 4, 1, 2]
    profits = [3, 5, 3, 2]
    k = 2
    w = 3
    print(findMaximizedCapital(k, w, profits, costs))
    costs = [5, 10, 10]
    profits = [7, 8, 60]
    k = 3
    w = 60
    print(findMaximizedCapital(k, w, profits, costs))
    
