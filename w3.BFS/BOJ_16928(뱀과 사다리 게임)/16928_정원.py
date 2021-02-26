# 31996	92
from collections import deque
from sys import stdin
board = [0] * 101
s_count, l_count = map(int, stdin.readline().split())

events = list(range(101)) # 뱀과 사다리 고려한 위치
for _ in range(s_count + l_count):
    start, end = map(int, stdin.readline().split())
    events[start] = end

def bfs(x):
    queue = deque()
    queue.append(x)

    while queue:
        a = queue.popleft()

        for i in range(1,7): # 1~6까지 주사위 나왔을 때 고려
            pos = a + i

            if pos > 100: continue # 조건1: 보드판 안에 위치
            pos = events[pos] # 뱀과 사다리 고려한 현재 위치

            if board[pos] == 0: # 조건2: 방문하지 않았다면
                board[pos] = board[a] + 1
                queue.append(pos)

    return board[100]

print(bfs(1))
