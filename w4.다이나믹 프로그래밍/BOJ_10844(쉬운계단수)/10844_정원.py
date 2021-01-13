# 28776KB	60ms
import sys

n = int(sys.stdin.readline()) # 1<= n <= 100

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# row는 길이, col는 끝자리 숫자를 나타냄
dp = [[0] * 10 for _ in range(n+1)]

# 길이가 1이면서 끝자리가 i인 숫자는 하나씩 밖에 없다 (1~9)
for i in range(1,10):
    dp[1][i] = 1

for i in range(2, n+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)
