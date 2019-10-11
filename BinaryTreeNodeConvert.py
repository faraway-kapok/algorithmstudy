"""将二叉搜索树转换为双向链表"""
#非递归版，中序遍历
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
         
        p = pRootOfTree
         
        stack = []
        resStack = []
         
        while p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                node = stack.pop()
                resStack.append(node)
                p = node.right
             
        resP = resStack[0]
        while resStack:
            top = resStack.pop(0)
            if resStack:
                top.right = resStack[0]
                resStack[0].left = top
         
        return resP



class Solution1:
    def Convert(self, root):
        if not root:
            return None
        if not root.left and not root.right:
            return root
         
        # 将左子树构建成双链表，返回链表头
        left = self.Convert(root.left)
        p = left
         
        # 定位至左子树的最右的一个结点
        while left and p.right:
            p = p.right
         
        # 如果左子树不为空，将当前root加到左子树链表
        if left:
            p.right = root
            root.left = p
         
        # 将右子树构造成双链表，返回链表头
        right = self.Convert(root.right)
        # 如果右子树不为空，将该链表追加到root结点之后
        if right:
            right.left = root
            root.right = right
             
        return left if left else root