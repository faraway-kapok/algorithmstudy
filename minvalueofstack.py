"""返回栈中的最小值，利用两个栈完成"""
class Solution:
    def __init__(self):
        self.arr = []
        self.m_min = []

    def push(self, node):
        minvalue = self.min()
        if not minvalue or node < minvalue:
            self.m_min.append(node)
        else:
            self.m_min.append(minvalue)
        self.arr.append(node)
    
    def pop(self):
        if self.arr:
            self.m_min.pop()
            return self.arr.pop()
    
    def top(self):
        if self.arr:
            return self.arr[-1]
    
    def min(self):
        if self.m_min:
            return self.m_min[-1]

if __name__ == "__main__":
    
# s = str([[1], [2,3,4], [5,[2,3]], [7], [0,[1,2,3,4],3,5], [1,3], [3,2,4]])
    s = input()

    res, count = 0, 0
    for i in range(len(s)):
        for j in s[i]:
            if j == '[':
                count += 1
                # print(count)
                res = max(res, count)
            if j == ']':
                count -= 1
    print(res) 