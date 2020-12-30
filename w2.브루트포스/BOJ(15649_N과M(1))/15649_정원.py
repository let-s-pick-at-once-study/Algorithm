# 96ms
import itertools
permutations = itertools.permutations

N , M = map(int, input().split())
pr = permutations(list(map(str, range(1,N+1))), M)

result = list(map(" ".join, pr))
[print(x) for x in result]

-------------------------------------------------------------------
# 92ms => input 형식을 readline형식으로 바꿔주니 4ms 절약!
import sys
import itertools
permutations = itertools.permutations

N , M = map(int, sys.stdin.readline().split())
pr = permutations(list(map(str, range(1,N+1))), M)

result = list(map(" ".join, pr))
[print(x) for x in result]
