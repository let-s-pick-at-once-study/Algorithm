# 29436KB 68ms
# 섬의 개수와 같은 방식으로 풀이

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
graph = [ list(map(int, [x for x in input()])) for _ in range(N) ]
visietd = [ [False] * N for _ in range(N) ]
num = 0
total_nums = []

def dfs(x, y):
    global  num
    num += 1
    visietd[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N) and (not visietd[nx][ny]) and (graph[nx][ny] == 1):
            dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(N):
        if not visietd[i][j] and graph[i][j] == 1:
            num = 0
            dfs(i, j)
            count += 1
            total_nums.append(num)

print(count)
# 오름차순 정렬 후 출력!
[print(x) for x in sorted(total_nums)]

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 64ms로 줄지만 29440KB로 증가
import sys
sys.setrecursionlimit(100000)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(sys.stdin.readline())
# input 함수로 받지 않으면 작동을 하지 않음! -> 런타임에러
graph = [ list(map(int, [x for x in input()])) for _ in range(N) ]
visietd = [ [False] * N for _ in range(N) ]
num = 0
total_nums = []

def dfs(x, y):
    global  num
    num += 1
    visietd[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < N) and (0 <= ny < N) and (not visietd[nx][ny]) and (graph[nx][ny] == 1):
            dfs(nx, ny)

count = 0
for i in range(N):
    for j in range(N):
        if not visietd[i][j] and graph[i][j] == 1:
            num = 0
            dfs(i, j)
            count += 1
            total_nums.append(num)

print(count)
[print(x) for x in sorted(total_nums)]
