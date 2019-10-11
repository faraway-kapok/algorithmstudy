class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""从上向下打印二叉树，二叉树的广度遍历"""
class Solution:

    def PrintFromTopToBottom(self, root):
            if not root:
                return []
            currentStack = [root]
            res = []
            while currentStack:
                nextStack = []
                for i in currentStack:
                    if i.left: nextStack.append(i.left)
                    if i.right: nextStack.append(i.right)
                    res.append(i.val)
                currentStack = nextStack
            print(res)

if __name__ == "__main__":
    node1 = TreeNode(8)
    node2 = TreeNode(6)
    node3 = TreeNode(10)
    node4 = TreeNode(5)
    node5 = TreeNode(7)
    node6 = TreeNode(9)
    node7 = TreeNode(11)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    s = Solution()
    s.PrintFromTopToBottom(node1)