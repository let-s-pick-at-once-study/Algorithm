# 35492KB	148ms

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
time = [0] * 100001 # 이동시간/거리 & 방문여부를 알기 위한 변수

def bfs(n, k):
    queue = deque([n])

    while queue:
        v = queue.popleft()

        if v == k:
            print(time[v])
            break

        for next_step in (v-1, v+1, v*2):
            if 0 <= next_step < 100001 and (not time[next_step]):
                time[next_step] = time[v] + 1
                queue.append(next_step)

bfs(N, K)
