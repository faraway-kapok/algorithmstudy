"""
两个队列实现栈功能
"""
from ArrayQueue import ArrayQueue

class TwoQueuesStack:
    def __init__(self):
        self.data = ArrayQueue()
        self.helpqueue = ArrayQueue()
    
    def push(self, pushint):
        self.data.add(pushint)
    
    def peek(self):
        if self.data.isEmpty():
            raise RuntimeError("Stack is empty")
        while (len(self.data) != 1):
            self.helpqueue.add(self.data.poll())
        
        res = self.data.poll()
        self.helpqueue.add(res)
        swap()
        return res
    
    def pop(self):
        if self.data.inEmpty():
            raise RuntimeError("Stack is empty")
        while len(self.data) > 1:
            self.helpqueue.add(self.data.poll())
        res = self.data.poll()
        swap()
        return res
    
    def swap():
        tmp = self.data
        self.data = self.helpqueue
        self.helpqueue = tmp

