# 48756	324
from sys import stdin
t = int(stdin.readline()) # 테스트 개수
num_list = []
for _ in range(t):
    num_list.append(int(stdin.readline()))    
max_num = max(num_list) # 가장 큰 값까지 dp 구하기

# dp[i][j] : i는 타겟 숫자 / j는 i를 만드는데 더해지는 끝자리 숫자
dp = [[0]*4 for _ in range(max_num+1)]
dp[1] = [0,1,0,0] # 1
dp[2] = [0,0,1,0] # 2
dp[3] = [0,1,1,1] # 2+1, 1+2, 3

for i in range(4, max_num + 1): # 행
    for j in range(1,4): # 열
        dp[i][j] = (sum(dp[i-j]) - dp[i-j][j]) % 1000000009

for num in num_list:
    print(sum(dp[num]) % 1000000009)
