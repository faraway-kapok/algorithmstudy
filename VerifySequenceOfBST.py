"""二叉搜索树的后序遍历序列"""
class Sosution:
    def VerifySequenceOfBST(self, sequence):
        if not sequence or len(sequence) <= 0:
            return False

        length = len(sequence)-1
        root = sequence[-1]
        #在二叉搜索树中，左子树节点小于根节点
        i = 0
        while i < length:
            if sequence[i] > root:
                break
            i += 1
        #在二叉搜索树中，右子树节点大于根节点
        for j in range(i, length):
            if sequence[j] < root:
                return  False
        #判断左子树是否为二叉搜索树
        left = True
        if i > 0 :
            left = self.VerifySequenceOfBST(sequence[0:i])
        #判断右子树是否为二叉搜索树
        right = True
        if i < length:
            right = self.VerifySequenceOfBST(sequence[i:-1])
        return (left and right)

    """二叉搜索树的前序遍历序列"""
    def verifyPreorder(self, preorder):
        if preorder:
            st, lower = [], -1<<30
            for e in preorder:
                if e < lower:
                    return False
                if st and e > st[-1]:
                    last = 0
                    while st and e > st[-1]:
                        last = st.pop()
                        lower = max(last, lower)
                    if not st:
                        lower = last
                st.append(e)
            return True
        return True