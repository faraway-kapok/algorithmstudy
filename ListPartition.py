"""
11.将单向链表按某值划分为左边小，中间相等，右边大的形式
"""

"""
给定一个单向链表的头结点head，节点的值类型是整型，在给定一个整数pivot，
实现一个调整链表的函数将链表调整为左部分都是值小于pivot的节点，
中间部分都是值等于pivot的节点，右部分都是值大于pivot的节点。
除此要求外，对调整后的节点顺序没有更多要求
"""

"""
进阶问题：
在原问题上添加两个要求
1.在左中右三个部分的内部也做顺序要求，要求每部分例的节点从左到右的顺序
与原链表中节点的先后顺序一致
例如，链表9->0->4->5->1,pivot=3,调整后的链表为0->1->9->4->5
2.如果链表长度为N， 时间复杂度请达到0(N)，额外空间复杂度请达到O(1)
"""
"""
准备六个变量，
小于的lessstart, lessend,等于的equalstart, equalend,大于的morestart,moreend

"""

def arrpartition(head, pivot):
    sh = None
    st = None
    eh = None
    et = None
    mh = None
    mt = None
    nextn = None
    while head != None:
        nextn = head.next
        head.next = None
        if head.value< pivot:
            if sh == None:
                sh = head
                st = head
            else:
                sh.next = head
                st = head
        elif head.value == pivot:
            if eh == None: 
                eh = head
                et = head
            else:
                eh.next = head
                et = head
        else:
            if mh == None:
                mh = head
                mt = head
            else:
                mh.next = head
                mt = head
        
        head = nextn
    
    if st != None:
        st.next = eh
        et = st if et == None else et
    if et != None:
        et.next = bh
    
    return sh if sh != None else if eh != None else bh