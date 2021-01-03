# 32928KB	96ms

from collections import deque
import sys
sys.setrecursionlimit(100000)

N, M, V = map(int, sys.stdin.readline().split())
graph = [ [] for _ in range(N+1) ]
for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
# 노드별로 오름차순으로 정렬
graph = [ sorted(x) for x in graph ]

def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end = " ")
    
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


def bfs(graph, v, visited):
    queue = deque([v])
    # 현재 노드 방문 처리
    visited[v] = True

    # 큐가 빌 때까지 반복
    while queue:
        # 큐의 맨 앞의 원소 뽑아 출력(FIFO)
        x = queue.popleft()
        print(x, end = " ")

        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


visited = [False] * (N+1)
dfs(graph, V, visited)

# visited 배열 초기화를 위해 한 번 더 작성
visited = [False] * (N+1)
print("")
bfs(graph, V, visited)
