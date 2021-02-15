# 68332	540
from sys import stdin
dp = [0] * 1000001 # n은 양수이며 1,000,000보다 작거나 같다
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 1000001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    print(dp[n])
