# 28776KB	64ms
import sys

N = int(sys.stdin.readline()) # 1 ≤ N ≤ 100,000,000

result = 0
x = 1

# 자릿수로 나누어 생각 / while문 돌때마다 x는 10의 배수만큼 증가
while x <= N:
    result += (N-x) + 1
    x *= 10

print(result)
