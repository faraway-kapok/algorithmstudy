"""
最小覆盖子串的查找，例如longstring ="abbccedscab"
alphabet ="abc",其中满足要求的字串为"cab"
1.滑动窗口
2.需统计alphabet中字符的相同个数，
需要同时满足字符以及字符数目的字串(隐藏条件)
"""
def minWindow(long_string, alphabet):
    if not long_string or not alphabet:
        return ""
    if len(long_string) < len(alphabet):
        return ""
    dict_al ={}
    for alpha in alphabet:
        dict_al[alpha] = dict_al.get(alpha, 0) + 1
    required_al = len(dict_al)
    print(required_al)

    filtered_s = []
    for i, char in enumerate(long_string):
        if char in dict_al:
            filtered_s.append((i,char))
    
    l, r = 0, 0
    formed = 0
    windows_counts = {}
    ans = (float("inf"), None, None)
    while r < len(filtered_s):
        character = filtered_s[r][1]
        windows_counts[character] = windows_counts.get(character, 0) + 1
        
        if windows_counts[character] == dict_al[character]:
            formed += 1
        while l <= r and formed == required_al:
            character = filtered_s[l][1]
            end = filtered_s[r][0]
            start = filtered_s[l][0]
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)
            windows_counts[character] -= 1
            if windows_counts[character] < dict_al[character]:
                formed -= 1
            l += 1
        r += 1
    return "" if ans[0] == float("inf") else long_string[ans[1]:(ans[2]+1)]

print(minWindow("aa","aa"))
