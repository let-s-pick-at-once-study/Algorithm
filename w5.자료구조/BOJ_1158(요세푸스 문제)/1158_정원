# 32676KB	92ms
import sys
from collections import deque
n, k = map(int,sys.stdin.readline().split())
queue = deque(list(range(1,n+1)))
answer = []

i = 0
while queue:
    if i == len(queue)-1:
        i = 0
    queue.rotate(-(k-1))
    x = queue.popleft()
    answer.append(x)
    i += 1

print("<" + str(answer).replace("[","").replace("]","") + ">")
