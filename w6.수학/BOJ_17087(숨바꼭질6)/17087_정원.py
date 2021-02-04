# 41872	124
from sys import stdin
import math

n, s = map(int, stdin.readline().split())
a_ls = map(int, stdin.readline().split())
result_ls = [abs(x - s) for x in a_ls]
ans = min(result_ls)
for x in result_ls:
   ans = math.gcd(x, ans)
print(ans)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 39756	136
from sys import stdin

n, s = map(int, stdin.readline().split())
a_ls = map(int, stdin.readline().split())
result_ls = [abs(x - s) for x in a_ls]
ans = min(result_ls)

# 유클리드 방식
def gcd(a, b):
    if b == 0: # 종료조건
        return a
    return gcd(b, a % b) # 좀 더 작은 값으로 자기 자신을 호출

for x in result_ls:
   ans = gcd(x, ans)

print(ans)
