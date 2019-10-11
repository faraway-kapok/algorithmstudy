"""给定一个字符串str，返回str中最长回文字串的长度"""
"""
1.暴力解法，适合奇偶数，时间复杂度为O(N*N)
在字符串的首位和中间分别添加一个字符例如"#",
从头开始计算以其为中心的回文长度，
返回最长的回文长度除以2，即为最终的回文字串长度
"""
"""
2.manacher方法， 时间复杂度为O(N)
a.回文半径数组，从0开始依次求取回文半径，放入数组组
b.最右回文半径，记录位置下到达的最右的回文位置
c.取得第一次到达最右回文位置的中心位置，
 即1213121，3到达的最右回文位置为6，b代表6，c代表3

思路：
1.如果i不在最右回文边界内，暴力扩，时间复杂度O(N)
2.如果i在最右回文边界内，求取i在c左边的对称点i'
2.1 i'的回文半径在L,R内部，即z[k(aba)tFt(aba)k]Y
    c指F的位置，i指b的位置 
    i位置的回文区域与i'相同，最右回文边界不用扩，时间复杂度为O(1)
2.2 i'的回文半径不在L,R内部，即(ab[cdcba)tTtabcdc]f
    中括号代表L,R,c指T的位置，i指d的位置，小括号代表i'的回文区域
    i的回文半径为i到R, 时间复杂度为O(1)
2.3 i'的回文半径与L压线，即t[(abcba)kKkabcba]k
    中括号代表L,R，c指K的位置，i指c的位置,小括号代表i'的回文区域
    i的回文半径首先i到R属于回文半径，但仍需要从R向右继续尝试是否存在回文，与第1中加起来， 时间复杂度O(N)
"""
def manacherstring(arr):
    res = [0] * (1+2*len(arr))
    index = 0
    for i in range(len(res)):
        if i & 1 == 0:
            res[i] = "#"
        else:
            res[i] = arr[index]
            index += 1
    return res
def maxLcpsLength(arr):
    if arr == None or len(arr) == 0:
        return 0
    chararr = manacherstring(arr)
    parr = [None] * len(chararr)
    C, R = -1, -1
    maxvalue = float('-inf')
    for i in range(len(chararr)):
        parr[i] =  min(parr[2*C - i], (R-i)) if R > i else 1
        while (i+parr[i] < len(chararr) and i-parr[i] > -1):
            if chararr[i+parr[i]] == chararr[i-parr[i]]:
                parr[i] += 1
            else:
                break
        if i+parr[i] > R:
            R = i + parr[i]
            C = i
        maxvalue = max(maxvalue, parr[i])
    return maxvalue - 1
"""一个字符串只能向后添加字符，如何使整个字符串成为回文，添加最少字符"""
"""找到第一个包含最后一个字符的回文串，前面非该回文串的部分逆序添加到字符串"""
def shortestEnd(arr):
    if arr == None or len(arr) == 0:
        return None
    chararr = manacherstring(arr)
    parr = [None] * len(chararr)
    index = -1
    pr = -1
    maxContainsEnd = -1
    for i in range(len(chararr)):
        parr[i] =  min(parr[2*index - i], (pr-i)) if pr > i else 1
        while (i+parr[i] < len(chararr) and i-parr[i] > -1):
            if chararr[i+parr[i]] == chararr[i-parr[i]]:
                parr[i] += 1
            else:
                break
        if i+parr[i] > pr:
            pr = i + parr[i]
            index = i
        if pr == len(chararr):
            maxContainsEnd = parr[i]
            break
        res = [None] * (len(arr) - maxContainsEnd + 1)
        for i in range(len(res)):
            res[len(res) -1 -i] = chararr[i*2 + 1]
        return res
if __name__ == "__main__":
    arr = 'abcd123321'
    print(shortestEnd(arr))