"""
前缀树
'abc', 'bcd','abd', 'def',头节点是否有走向a, b, c, d 的路径
用法：
1.查询是否有'be'开头的字符串
2.查询是否添加过'be' #添加以该节点为结尾的字符串的个数可以实现
3.有多少个字符串以'bc'为前缀 #添加每个节点被滑过的次数来实现
都可以通过添加数据项来完成查询
"""
class TridNode:
    def __init__(self):
        #多少字符串到达此节点
        self.path = 0
        #多少字符串以它为结尾
        self.end = 0
        #假设只有小写字母开头的路，共26条路
        self.next = [None] * 26

class Trie:
    def __init__(self):
        """the root node to Trie"""
        self.root = TridNode()
    
    def insert(self, word):
        node = self.root
        if word == None:
            return
        chs = list(word)
        index = 0
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if node.next[index] == None:
                node.next[index] = TridNode()
            node = node.next[index]
            node.path += 1

        node.end += 1
    
    def delete(self, word):
        if self.search(word) != 0:
            chs = list(word)
            node = self.root
            index = 0
            for i in range(len(word)):
                index = ord(chs[i]) - ord('a')
                node.next[index].path -= 1
                if node.next[index].path == 0:
                    node.next[index] = None
                    return
                node = node.next[index]
            node.end -= 1
    #插入多少次word
    def search(self, word):
        if word == None:
            return
        chs = list(word)
        node = self.root
        index = 0
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if node.next[index] == None:
                return 0
            node = node.next[index]
        return node.end
    
    def prefixNumber(self, pre):
        if pre == None:
            return
        chs = list(pre)
        node = self.root
        index = 0
        for i in range(len(chs)):
            index = ord(chs[i]) - ord('a')
            if node.next[index] == None:
                return 0
            node = node.next[index]
        return node.path
        

if __name__ == "__main__":
    trie = Trie()
    print(trie.search('zuo'))
    trie.insert('zuo')
    print(trie.search('zuo'))
    trie.delete('zuo')
    print(trie.search('zuo'))
    trie.insert('zuo')
    trie.insert('zuo')
    trie.delete('zuo')
    print(trie.search('zuo'))
    trie.delete('zuo')
    trie.insert('zuoa')
    trie.insert('zuoac')
    trie.insert('zuoab')
    trie.insert('zuoad')
    trie.delete('zuoa')
    print(trie.search('zuoa'))
    print(trie.prefixNumber('zuo'))



    