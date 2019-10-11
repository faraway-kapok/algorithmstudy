"""
13.复制含有随机指针节点的链表,复杂链表的复制
"""
"""
一种特殊的链表节点描述如下:
public class cur
{public int value; 
public cur next; 
public cur rand;}
public cur(int data)
{this.value=data;}
cur中的value是节点值，
next指针和正常链表中的next指针含义一样
rand指针可能指向链表中的任一个节点，有可能指向null
给定一个有cur节点类型组成的无环单链表的头节点head
请实现，一个函数完成链表中所有结构的复制，并返回复制的新
链表的头节点
进阶：
不使用额外的数据结构，只用有限几个变量，且时间复杂度为O(N)
完成原问题要实现的函数
"""
"""
1.遍历整个链表将cur跟value放到map里，得到cur的拷贝节点
"""
class Node:
    def __init__(self, val, nex, rand):
        self.val = val
        self.next = nex
        self.rand = rand
        
#python中的字典相当于java中的hashmap
def copyListWithRand1(head):
    if head == None:
        return None
    memories = {}#该字典中，key代表旧链表的节点，val代表新链表的节点
    cur = head
    while cur != None:
        cloneNode = Node(cur.val, None, None)
        memories[cur] = cloneNode
        cur = cur.next
    cur = head
    while cur != None:
        #用dict.get因若key为空的话，默认返回None
        #根据字典映射关系处理新链表的rand和next关系
        memories.get(cur).next = memories.get(cur.next)
        memories.get(cur).rand = memories.get(cur.rand)
        cur = cur.next
    return memories[head]

#将一个节点的拷贝节点放到其后面，即将next指向其拷贝节点
#拷贝rand节点，
#分离
def copyListWithRand2(head):
    if head == None:
        return None
    cur = head
    while cur:
        clone = Node(cur.val, cur.next, None)
        curNext = cur.next
        cur.next = clone
        cur = curNext
    
    cur = head
    while cur:
        if cur.rand == None:
            cur.next.rand = None
        else:
            cur.next.rand = cur.rand.next
        cur = cur.next.next

    cur = head
    newHead = head.next
    while cur.next:#空节点没有next节点
        curNext = cur.next
        cur.next = cur.next.next
        cur = curNext
    return newHead


