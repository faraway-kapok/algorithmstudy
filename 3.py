import re

def splitchar(s):
    res = re.sub("--", " ", s)
    res = re.sub("[^a-zA-Z0-9-]", " ", res)
    res = re.sub("- ", " ", res)
    res = re.sub(" -", " ", res)

    res = res.split(" ")
    print(res)
    for i in range(len(res)-1,-1,-1):
        if res[i] != "":
            print(res[i], end=" ")

# s = input()
# splitchar(s)


def countarr(arr):
    arrdic = {}
    for ele in arr:
        if ele not in arrdic:
            arrdic[ele] = 1
        else:
            arrdic[ele] += 1
    return arrdic

s = input().strip()
arrdic = countarr(s)
arrdic = sorted(arrdic.items(), key=lambda x:x[0])
res = ""
for key, value in arrdic:
    res += str(key) + str(value)
print(res)