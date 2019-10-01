s = input().split(" ")
arr = []
arrdic = {}
t = len(s)
for i in range(t):
    data = int(s[i])
    arr.append(data)
    arrdic[data] = i
arr = sorted(arr)
count = 0
for i in range(t-1):
    if arrdic[arr[i]] > arrdic[arr[i+1]]:
        arrdic[arr[i+1]] = t+1
        count += 1
print(count)