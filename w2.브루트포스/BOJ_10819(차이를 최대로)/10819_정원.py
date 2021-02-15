# 28776	172
from itertools import permutations
from sys import stdin

n = int(stdin.readline()) # 3 ≤ N ≤ 8 => 완전탐색 가능
nums = list(map(int, stdin.readline().split()))
result = 0

for p in permutations(nums, n):
    # 인덱스별 차이 합계 임시 저장
		temp = 0
    for i in range(n-1):
        temp += abs(p[i] - p[i+1])
		
		# result 업데이트
    result = max(result, temp)

print(result)
