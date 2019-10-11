"""
KMP算法
abcabcd: d之前的最长前缀跟最长后缀的匹配信息的长度为3，
最长前缀不包含c，最长后缀不包含a
即next_arr=[-1,0,0,1,2,3,3],
分别为abcabcd的最长前缀和最长后缀匹配的长度列表
思路：
当match字符串与arr字符串存在不匹配时，arr中的指针p1不变
match中的指针p2指向该指针对应位置的最长前缀的下一个位置，例如：
假设不匹配位置为d，p2指向a位置
arr中p1位置与match中p2位置继续匹配，当又出现不匹配且最长前缀为-1时，
丢弃p1之前的所有位置，p2回到match的开始，与p1位置重新开始匹配
"""
def getIndexOf(arr, match):
    if arr == None or match == None or len(match) < 1 \
        or len(arr) < len(match):
        return -1
    p1, p2 = 0, 0
    nextarr = getNextArray(match)
    while p1 < len(arr) and p2 < len(match):
        if arr[p1] == match[p2]:
            p1 += 1
            p2 += 1
        elif nextarr[p2] == -1: #即match的第一字符就与arr中不匹配
            p1 += 1
        else:
            p2 = nextarr[p2]
    return p1-p2 if p2 == len(match) else -1
"""获取最长前缀长度"""
def getNextArray(match):
    if len(match) == 1:
        return [-1]
    nextarr = []
    nextarr[0] = -1
    nextarr[1] = 0
    i = 2
    cn = 0 #跳的位置
    while i < len(match):
        if match[i-1] == match[cn]:
            cn += 1
            nextarr[i] = cn 
            i += 1
        elif cn > 0:
            cn = nextarr[cn]
        else:
            nextarr[i] = 0
            i += 1
    return nextarr
    