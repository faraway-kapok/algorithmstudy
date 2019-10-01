"""
用数组结构实现大小固定的队列和栈
"""
"""index 永远指向下一个数入栈的地方"""
class ArrayStack:
    def __init__(self,initSize=100):
        if initSize < 0:
            raise ValueError("This init size is less than 0")
        self.arr = [None] * initSize
        self.index = 0

    #返回栈顶
    def peek(self):
        if self.index == 0:
            return None
        return self.arr[self.index-1]
    #入栈
    def push(self, x):
        if self.index == len(self.arr):
            raise RuntimeError("The stack is full")
        self.arr[self.index] = x
        self.index += 1
    #出栈
    def pop(self):
        if self.index == 0:
            raise RuntimeError("The stack is empty")
        self.index -= 1
        return self.arr[self.index]

    def isEmpty(self):
        if self.index == 0:
            return True
        else:
            return False

    

if __name__ == "__main__":
    arrstack = ArrayStack(4)
    testlist = [1,2,3,4]
    for i in testlist:
        arrstack.push(i)
    print(arrstack.peek())
    for j in range(11):
        print(arrstack.pop())
    arrstack.push(20)
    print(arrstack.peek())