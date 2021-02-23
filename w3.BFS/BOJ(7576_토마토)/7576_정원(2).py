# 98824	2328
from sys import stdin
from collections import deque

m, n = map(int, stdin.readline().split())
box = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [-1,0,0,1]
dy = [0,1,-1,0]

def bfs():
    queue = deque()
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1: # 탐색을 위한 시작 위치 선정
                queue.append((i,j))

    while queue:
        a,b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n and 0 <= ny < m) and (box[nx][ny] == 0): # 0은 안익은 토마토를 뜻함과 동시에 방문되지 않았다는 것을 뜻함
                box[nx][ny] = box[a][b] + 1 # 안익은 토마토를 익은 토마토로 & 날짜수 +1
                queue.append((nx,ny))
    return box

def cal_count(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1
            else:
                count = max(count, graph[i][j]-1) # -1을 하는 이유는 날짜수 처음 시작이 0이 아닌 1로 시작했기 때문
    return count

bfs()
print(cal_count(box))
