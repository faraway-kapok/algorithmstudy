"""
两个栈实现队列
"""
from Arraystack import ArrayStack
class TwoStacksQueue:
    def __init__(self):
        self.stackPush = ArrayStack()
        self.stackPop = ArrayStack()

    def push(self,pushint):
        self.stackPush.push(pushint)
    
    def poll(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            raise RuntimeError("Queue is empty")
        elif self.stackPop.isEmpty():
            while (not self.stackPush.isEmpty()):
                self.stackPop.push(self.stackPush.pop())

        return self.stackPop.pop()
    
    def peek(self):
        if self.stackPop.isEmpty() and self.stackPush.isEmpty():
            raise RuntimeError("Queue is empty")
        elif self.stackPop.isEmpty():
            while (not self.stackPush.isEmpty()):
                self.stackPop.push(self.stackPush.pop())

        return self.stackPop.peek()
