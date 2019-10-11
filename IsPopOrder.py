"""某序列是否为出栈顺序"""
class Solution:
    def IsPopOrder(self, pushV, popV):
        stack = []
        while popV:
            
            if pushV and popV[0] == pushV[0]:
                
                popV.pop(0)
                pushV.pop(0)
            elif stack and popV[0] == stack[-1]:
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True

pushV = [1,2,3,4,5]
popV = [4,5,3,2,1]

s = Solution()
print(s.IsPopOrder(pushV, popV))