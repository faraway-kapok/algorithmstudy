# s = input()


def findpair(arr1,arr2, R):
    p1 = 0
    p2 = 0
    length1 = len(arr1)
    length2 = len(arr2)
    temp = []
    while p1 < length1 and p2 < length2:
        
        if arr1[p1] <= arr2[p2]:
            tmpp2 = p2
            while arr2[p2]-arr2[p1] <= R and tmpp2 < length2:
                temp.append((arr1[p1],arr2[tmpp2]))
                tmpp2 += 1
            if (arr2[p2]-arr1[p1]) > R:
                temp.append((arr1[p1],arr2[p2]))
            p1 += 1
        else:
            p2 += 1
    while p1 < length1:
        if arr1[p1] <= arr2[p2-1] and (arr2[p2]-arr1[p1]) <= R:
            temp.append((arr1[p1], arr1[p2-1]))
        p1 += 1
    return temp

s = input().split("},")
import re
ns = []
for i in s:
    n = re.findall('\d{1,5}',i)
    ns.append(n)
print(ns)
arr1 = []
arr2 = []
for i in ns[0]:
    arr1.append(int(i))
print(arr1)
for j in ns[1]:
    arr2.append(int(j))
print(arr2)
R = int(ns[2][0])
res = findpair(arr1, arr2, R)
for i in res[:-1]:
    print(i, end=',')
print(res[-1])