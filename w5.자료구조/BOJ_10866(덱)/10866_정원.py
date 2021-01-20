# 32716KB	104ms
from sys import stdin
from collections import deque
queue = deque()

for _ in range(int(stdin.readline())):
    commands = stdin.readline().split()
    cmd = commands[0]
    if cmd == "push_front":
        queue.appendleft(commands[1])
    elif cmd == "push_back":
        queue.append(commands[1])
    elif cmd == "pop_front":
        x = queue.popleft() if queue else -1
        print(x)
    elif cmd == "pop_back":
        x = queue.pop() if queue else -1
        print(x)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(1 - int(bool(queue)))
    elif cmd == "front":
        x = queue[0] if queue else -1
        print(x)
    elif cmd == "back":
        x = queue[-1] if queue else -1
        print(x)
