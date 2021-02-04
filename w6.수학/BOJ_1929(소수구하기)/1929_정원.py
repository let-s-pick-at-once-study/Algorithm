# 135400	1008
from sys import stdin
first, last = map(int, stdin.readline().strip().split()) # (1 ≤ M ≤ N ≤ 1,000,000)
# first가 1이면 2로 바꿔준다 (소수는 2부터 시작)
first = 2 if first == 1 else first
prime_set = set(range(first, last+1))

# 에라토네스의 체
for i in range(2, last+1):
  prime_set -= set(range(i*i, last+1, i))

# set는 dict와 마찬가지로 순서가 없기 때문에, list로 바꾼 뒤 정렬해서 출력해야 함
[print(x) for x in sorted(list(prime_set))]
