"""
返回n!的最后一位不为零的数
"""
n = int(input())
if len(n) == 0:
    print(None)
res = 1
for i in range(2,n+1):
    res *= i
    while(res%10 == 0):
        res //= 10
    res %= 100000
print(res%10)