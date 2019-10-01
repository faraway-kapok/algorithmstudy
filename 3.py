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

s = input()
splitchar(s)
