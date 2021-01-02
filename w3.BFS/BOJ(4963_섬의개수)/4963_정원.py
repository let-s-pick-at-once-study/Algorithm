import sys
sys.setrecursionlimit(10000)

dx = [1,-1,0,0,1,-1,1,-1]
dy = [0,0,1,-1,1,-1,-1,1]

def dfs(x, y):
    visited[x][y] = True

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < h) and (0 <= ny < w) and (not visited[nx][ny]) and (s[nx][ny] == 1):
            dfs(nx, ny)


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break

    s = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]

    count = 0
    for i in range(h):
        for j in range(w):
            if (not visited[i][j]) and (s[i][j] == 1):
                dfs(i, j)
                count += 1
    print(count)
