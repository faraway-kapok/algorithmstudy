"""
判断是否为回文数组
"""

"""
方法一，直接压栈，空间为O(n)
"""
from Arraystack import ArrayStack
from Node import Node
class isPalindrome1:
    def __init__(self, head):
        self.head = head
        self.cur = head
        self.stack = ArrayStack()
    
    def ispalindrome1(self):
        while self.cur != None:
            self.stack.push(self.cur)
            self.cur = self.cur.next
        while self.head != None:
            if self.head.value != self.stack.pop().value:
                return False
            self.head = self.head.next
        return True

class isPalindrome2:
    def __init__(self, head):
        self.head = head
        self.right = head.next
        self.cur = head
    
    def ispalindrome2(self):
        if self.head == None or self.head.next ==None:
            return True
        while self.cur.next != None and self.cur.next.next != None:
            self.right = self.right.next
            self.cur = self.cur.next.next
        self.stack = ArrayStack()
        while self.right != None:
            self.stack.push(self.right)
            self.right = self.right.next
        
        while not self.stack.isEmpty():
            if self.head.value != self.stack.pop().value:
                return False
            self.head = self.head.next
        
        return True


class isPalindrome3:
    def __init__(self, head):
        self.head = head
        self.n1 = head
        self.n2 = head
        self.res = True
        self.n3 = Node(None)

    def ispalindrome3(self):
        if self.head == None or self.head.next == None:
            return True
        #找到中点，奇数个找到中间点，偶数个找到第二个点
        while self.n2.next != None and self.n2.next.next != None:
            self.n1 = self.n1.next
            self.n2 = self.n2.next.next
        
        self.n2 = self.n1.next #n2指向右半部分的第一个节点
        self.n1.next = None # 中点的next置为空
        
        #后半部分逆序
        while self.n2 != None:
            self.n3 = self.n2.next
            self.n2.next = self.n1
            self.n1 = self.n2
            self.n2 = self.n3
        
        self.n3 = self.n1 #保存最后一个节点
        self.n2 = self.head #n2指向左部分第一个节点
        
        while self.n1 != None and self.n2 != None:
            if self.n1.value != self.n2.value:
                self.res = False
                break

            self.n1 = self.n1.next #从右向左走向中间
            self.n2 = self.n2.next#从左向右走向中间
        
        self.n1 = self.n3
        self.n3.next = None
        #将链表逆序回来
        while (self.n1 != None):
            self.n2 = self.n1.next
            self.n1.next = self.n3
            self.n3 = self.n1
            self.n1 = self.n2
        
        return self.res





