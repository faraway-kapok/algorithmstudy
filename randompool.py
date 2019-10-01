"""
设计RandomPool结构
设计一种结构，在该结构中添加如下三个功能：
insert(key):将某个key加入到该结构中，做到不重复加入
delete(key):将原本在结构中的某个key移除，
getRandom():等概率随机返回结构中的任何一个key
要求：insert，delete和getRandom方法的时间复杂度都为O(1)
"""
import random
class pool:
    def __init__(self):
        self.map1 = {}
        self.map2 = {}
        self.size = 0
    
    def insertkey(self, k):
        self.map1[k] = self.size
        self.map2[self.size] = k
        self.size += 1
    def deletekey(self, k):
        if k in self.map1:
            index = self.map1[k]
            lastkey = self.map2[self.size-1]
            self.map2[index] = lastkey
            self.map1[lastkey] = index
            del self.map1[k]
            del self.map2[self.size-1]
            self.size -= 1
    def getRandom(self):
        if self.size == 0:
            return None
        index = int(random.random()*self.size)
        return self.map2.get(index)

if __name__ == "__main__":
    randompool = pool()
    randompool.insertkey(8)
    randompool.insertkey(100)
    randompool.insertkey(34)
    randompool.insertkey(4)
    randompool.insertkey(5)
    randompool.insertkey(24)
    print(randompool.getRandom())
