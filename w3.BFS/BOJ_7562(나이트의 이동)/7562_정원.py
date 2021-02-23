from sys import stdin
from collections import deque

dx = [-2,-2,-1,-1,1,1,2,2] # x축
dy = [1,-1,2,-2,2,-2,1,-1] # y축

def bfs(x,y,r,c):
    visited[x][y] = True
    queue = deque()
    queue.append((x,y))

    while queue:
        a, b = queue.popleft()

        if a == r and b == c:
            return board[a][b]

        for i in range(8):
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n and 0 <= ny < n) and visited[nx][ny] == False:
                visited[nx][ny] = True
                board[nx][ny] = board[a][b] + 1
                queue.append((nx,ny))

for _ in range(int(stdin.readline())): # 테스트 케이스
    n = int(stdin.readline()) # 체스보드 길이
    board = [[0 for _ in range(n)] for _ in range(n)] # 체스보드 생성
    visited = [[False for _ in range(n)] for _ in range(n)] # 방문여부 확인
    x,y = map(int, stdin.readline().split()) # 출발 지점
    r,c = map(int, stdin.readline().split()) # 도착 지점

    print(bfs(x,y,r,c))
