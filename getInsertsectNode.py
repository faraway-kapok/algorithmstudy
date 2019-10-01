"""两个单链表相交的一系列问题"""
"""
本题中，单链表可能有环，可能无环
给定两个单链表的头结点head1，head2，这两个链表可能相交
也可能不相交
实现一个函数：如果两个链表相交，返回相交的第一个节点；
如果不相交，返回None
要求：如果链表长度为N， 链表2长度为M，时复达到O(N+M),
额复为O(1)
"""
"""
1.判断链表是否有环，快指针走两步，慢指针走一步，相遇则有环
此时，将快指针放到头结点，快指针走一步，相遇即入环点
2.链表一个有环，一个无环的情况，查找相交状况
分别遍历两链表，记录长度length与end，若end相等则相交，
若链表1较长链表1先走len1-len2步，若链表2较长链表2先走
len2-len1步，然后同时走，两链表第一次走到一起的点，
为第一个相交点;
若end不相等，则不相交
3.链表都有环,可能相交，可能不相交
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def iscircle(head):
    if head == None:
        return False
    p1 = head
    p2 = head
    loopexist = False
    while p2.next != None and p2.next.next != None:
        p1 = p1.next
        p2 = p2.next.next
        if p1 != p2:
            continue
        else:
            loopexist = True
            p2 = head
            while p1 != p2:
                p2 = p2.next
                p1 = p1.next
            print(p1)
            return p1
    return False

def getLoopNode(head):
    if head == None or head.next == None or head.next.next == None:
        return None
    p1 = head.next
    p2 = head.next.next
    while p1 != p2:
        if p2.next == None or p2.next.next == None:
            return None
        p2 = p2.next.next
        p1 = p1.next
    p2 = head
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1

def noloop(head1,head2):
    if head1 == None or head2 == None:
        return  None
    cur1 = head1
    cur2 = head2
    n = 0
    while cur1.next != None:
        n += 1
        cur1 = cur1.next
    while cur2.next != None:
        n -= 1
        cur2 = cur2.next
    if cur1 != cur2:
        return None
    cur1 = head1 if n > 0 else head2
    cur2 = head2 if cur1 == head1 else head1
    n = abs(n)
    while n != 0:
        n -= 1
        cur1 = cur1.next
    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

def bothloop(head1, loop1, head2, loop2):
    cur1 = None
    cur2 = None
    if loop1 == loop2:
        cur1 = head1
        cur2 = head2
        n = 0
        while cur1 != loop1:
            n += 1
            cur1 = cur1.next
        while cur2 != loop2:
            n -= 1
            cur2 = cur2.next
        cur1 = head1 if n > 0 else head2
        cur2 = head2 if cur1 == head1 else head1
        n = abs(n)
        while n != 0:
            n -= 1
            cur1 = cur1.next
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
    else:
        cur1 = loop1.next
        while cur1 != loop1:
            if cur1 == loop2:
                return loop1
            cur1 = cur1.next
        return None


def getInsertsectNode(head1,head2):
    if head1 == None or head2 == None:
        return None
    loop1 = getLoopNode(head1)
    loop2 = getLoopNode(head2)
    if loop1 == None and loop2 == None:
        return noloop(head1, head2)
    if loop1 != None and loop2 != None:
        return bothloop(head1, loop1, head2, loop2)
    return None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)
    node14 = Node(14)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node3

    node7.next = node8
    node8.next = node9
    node9.next = node10
    node10.next = node5

    print(getInsertsectNode(node1,node7))
   
