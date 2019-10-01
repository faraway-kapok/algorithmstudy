"""
实现一个特殊的栈， 在实现栈的基本功能的基础上，
再实现返回栈中最小元素的操作
要求:
1.pop, push, getMin操作的时间复杂度都是O(1)
2.设计的栈类型可以使用现成的栈结构
"""
"""
方法1：
两个栈，一个data栈，一个min栈
一个数压入栈，如果数大于min栈的栈顶，
data栈压入数，min栈压入栈顶相同数;
一个数弹出栈，min栈同时弹出;
min栈顶就是最小的元素
"""
from Arraystack import ArrayStack

class mystack1:
    def __init__(self):
        self.stackData = ArrayStack()
        self.stackMin = ArrayStack()
        self.newMin = 0
    
    def push(self, newNum):
        if self.stackMin.isEmpty():
            self.stackMin.push(newNum)
        elif newNum < self.getmin():
            self.stackMin.push(newNum)
        else:
            self.newMin = self.stackMin.peek()
        
        self.stackData.push(newNum)
    
    def pop(self):
        if self.stackData.isEmpty():
            raise RuntimeError("Your stack is empty")
        self.stackMin.pop()
        return self.stackData.pop()
    
    def getmin(self):
        if self.stackMin.isEmpty():
            raise RuntimeError("Your stack is empty")
        return self.stackMin.peek()