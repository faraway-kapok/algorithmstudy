"""
KMP算法
abcabcd: d之前的最长前缀跟最长后缀的匹配信息的长度为3，最长前缀不包含c，最长后缀不包含a
即next_arr=[-1,0,0,1,2,3,3],分别为abcabcd的最长前缀和最长后缀匹配的长度列表
"""