# 32076KB	104ms
# 최단경로 탐색할 때는 주로 BFS 사용해서 풀이

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
graph = [list(map(int, [x for x in stdin.readline().rstrip()])) for _ in range(N)]
check = [ [0] * M for _ in range(N) ]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque([[x, y]])
    check[x][y] = 1

    while queue:
        x, y = queue.popleft()

        if x == N - 1 and y == M - 1:
            return check[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M) and (check[nx][ny] == 0) and (graph[nx][ny] == 1):
                check[nx][ny] = check[x][y] + 1
                queue.append([nx, ny])

print(bfs(0, 0))
