"""获取最小的K个数"""
import heapq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == [] or k > len(tinput) or k <= 0:
            return []
        heapq.heapify(tinput)
        res = []
        for i in range(k):
            res.append(heapq.heappop(tinput))
        return res




class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if tinput == [] or k > len(tinput):
            return []
        tinput.sort()
        return tinput[: k]