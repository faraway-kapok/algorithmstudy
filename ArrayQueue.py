"""
用数组结构实现大小固定的队列和栈
"""
class ArrayQueue:
    def __init__(self,initSize=10):
        if initSize < 0:
            raise ValueError("This init size is less than 0")
        self.arr = [None] * initSize
        self.start = 0
        self.end = 0
        self.size = 0


    #返回队列顶端
    def peek(self):
        if self.size == 0:
            return None
        return self.arr[self.start]
    #入队列
    def push(self, x):
        if self.size == len(self.arr):
            raise IndexError("The queue is full")
        self.size += 1
        self.arr[self.end] = x
        self.end = self.end+1 if self.end != (len(self.arr)-1) else 0
        
    #弹出
    def poll(self):
        if self.size == 0:
            return False
            # raise IndexError("The queue is empty")
        self.size -= 1
        tmp = self.start
        # self.start += 1
        self.start = self.start+1 if self.start != (len(self.arr)-1) else 0
        return self.arr[tmp]
    
    def isEmpyt(self):
        if self.size == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    arrque = ArrayQueue(10)
    testlist = [1,2,3,4,5,6,7,9,8,10]
    for i in testlist:
        arrque.push(i)
    print(arrque.peek())
    for j in range(11):
        print(arrque.poll())
    arrque.push(20)
    print(arrque.peek())

