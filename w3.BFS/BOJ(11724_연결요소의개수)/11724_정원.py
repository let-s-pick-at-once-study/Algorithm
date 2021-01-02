# 63760KB	788ms

import sys
# 재귀 허용치 넘어가면 런타임 에러!
sys.setrecursionlimit(10000)
# n은 정점개수, m은 간선개수
n, m = map(int, sys.stdin.readline().split()) 

# DFS & 인접리스트 활용
# 노드와 인덱스 값을 맞춰주기 위해 (n+1)개의 리스트를 만들고 0번째는 사용 안함
adj = [ [] for _ in range(n + 1) ]
visited = [False] * (n + 1)

# 인접리스트 채우기
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    # 무방향 그래프이기 때문에 양쪽 모두 채워주어야 함
    adj[a].append(b)
    adj[b].append(a)

# 노드 방문시 visited 배열에 해당 인덱스 값 방문여부 체크
def dfs(node):
    visited[node] = True
    for i in adj[node]:
        if not visited[i]:
            dfs(i)

# 1부터 n까지 노드를 순회하며 방문여부를 확인 -> 방문이 안돼있다는 건 연결요소가 아니라는 뜻으로 카운트 증가
count = 0
for i in range(1, n + 1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
