# 32756 112
from collections import deque
from sys import stdin

n = int(stdin.readline())
board = [[-1 for _ in range(n)] for _ in range(n)] # 체스보드 구성
visited = [[False for _ in range(n)] for _ in range(n)] # 방문여부 확인
# 방향 변수
dx = [-2,-2,0,0,2,2] # 가로축
dy = [-1,1,-2,2,-1,1] # 세로축
    
def bfs(x, y, r, c): # x,y는 시작좌표 / r,c는 도착좌표 
    board[x][y] = 0 # 보드의 초기값이 -1이었기 때문에, 조건에 부합한다면 0으로 세팅해주어야 함
    visited[x][y] = True
    queue = deque() # 큐 생성
    queue.append((x,y))

    while queue: # 큐가 빌때까지 수행
        a,b = queue.popleft()

        if (a == r) and (b == c): 
            return board[a][b] # 도착지점에 도달한다면
            
        for i in range(6): # 방향 변수 개수만큼 반복            
            nx = a + dx[i]
            ny = b + dy[i]

            if (0 <= nx < n and 0 <= ny < n) and (visited[nx][ny] == False):
                visited[nx][ny] = True
                board[nx][ny] = board[a][b] + 1 # 이동횟수 구하기에 해당
                queue.append((nx,ny))

    return board[r][c] # 도착지점에 도달하지 못한다면

x,y,r,c = map(int, stdin.readline().split())    
print(bfs(x,y,r,c))
