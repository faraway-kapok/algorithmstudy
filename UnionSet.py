"""
并查集,当查询次数和合并次数达到O(N)级别时，
单次合并查询平均时间为O(1)
主要体现一种思路，当处理一个较大的岛问题时，可
将岛分为不同的模块，判断边界问题进行岛的合并，
实现最终的岛计算
"""
class Node:
    pass
class UnionFindSet:
    def __init__(self, nodes):
        self.makeSets(nodes)
        self.fathermap = {}
        self.sizemap = {}
    
    def makeSets(self, nodes):

        for node in nodes:
            self.fathermap[node] = node
            self.sizemap[node] = 1
    
    def findHead(self, node):
        father = self.fathermap.get(node)
        if father != node:
            father = self.findHead(father)
        self.fathermap[node] = father
        return father
    
    def issameset(self, a, b):
        return self.findHead(a) == self.findHead(b)
    
    def union(self, a, b):
        if a == None or b == None:
            return
        ahead = self.findHead(a)
        bhead = self.findHead(b)
        if ahead != bhead:
            asetsize = self.sizemap.get(ahead)
            bsetsize = self.sizemap.get(bhead)
            if asetsize <= bsetsize:
                self.fathermap[ahead] = bhead
                self.sizemap[bhead] = asetsize + bsetsize
            else:
                self.fathermap[bhead] = ahead
                self.sizemap[ahead] = asetsize + bsetsize
