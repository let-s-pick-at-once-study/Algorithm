import sys
sys.setrecursionlimit(10**5)

# 방향(좌,우,위,아래 + 대각선)
dx = [-1, 1, 0, 0, -1, 1, -1, 1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]

def dfs(x,y):
    visit[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w) and (not visit[nx][ny]) and (graph[nx][ny] == 1):
            graph[nx][ny] = 0
            dfs(nx, ny)

while (True):
    w, h = map(int, sys.stdin.readline().split())

    # 종료 조건
    if w == 0 and h == 0:
        break

    visit = [ [False] * w for _ in range(h) ]
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    count = 0
    for i in range(h):
        for j in range(w):
            if not visit[i][j] and graph[i][j] == 1:
                dfs(i, j)
                count += 1
    print(count)
