# 34036KB	100ms
import sys
from collections import deque
n = int(sys.stdin.readline())
commands = [list((sys.stdin.readline().split())) for _ in range(n)]
queue = deque()

def push(value):
    global queue
    queue.append(value)

def pop():
    global queue
    if queue:
        x = queue.popleft()
        print(x)
    else:
        print(-1)

def size():
    print(len(queue))

def empty():
    if queue:
        print(0)
    else:
        print(1)

def front():
    if queue:
        print(queue[0])
    else:
        print(-1)

def back():
    if queue:
        print(queue[len(queue)-1])
    else:
        print(-1)

def solution(command):
    cmd = command[0]
    if cmd == "push":
        push(command[1])
    elif cmd == "pop":
        pop()
    elif cmd == "size":
        size()
    elif cmd == "empty":
        empty()
    elif cmd == "front":
        front()
    elif cmd == "back":
        back()

for i in range(n):
    solution(commands[i])
    
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 33988KB	100ms
import sys
from collections import deque
n = int(sys.stdin.readline())
commands = [list((sys.stdin.readline().split())) for _ in range(n)]
queue = deque()

def solution(command):
    global queue
    cmd = command[0]

    if cmd == "push":
        queue.append(command[1])
    elif cmd == "pop":
        x = queue.popleft() if queue else -1
        print(x)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if queue else 1)
    elif cmd == "front":
        print(queue[0] if queue else -1)
    elif cmd == "back":
        print(queue[len(queue)-1] if queue else -1)

for i in range(n):
    solution(commands[i])
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 31996KB	92ms
import sys
from collections import deque
queue = deque()

for _ in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline().split()
    cmd = commands[0]
    if cmd == "push":
        queue.append(commands[1])
    elif cmd == "pop":
        x = queue.popleft() if queue else -1
        print(x)
    elif cmd == "size":
        print(len(queue))
    elif cmd == "empty":
        print(0 if queue else 1)
    elif cmd == "front":
        print(queue[0] if queue else -1)
    elif cmd == "back":
        print(queue[-1] if queue else -1)
 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 # 28776KB	76ms
import sys
arr = []

for _ in range(int(sys.stdin.readline())):
    commands = sys.stdin.readline().split()
    cmd = commands[0]
    if cmd == "push":
        arr.append(commands[1])
    elif cmd == "pop":
        x = arr.pop(0) if arr else -1
        print(x)
    elif cmd == "size":
        print(len(arr))
    elif cmd == "empty":
        print(1-int(bool(arr)))
    elif cmd == "front":
        print(arr[0] if arr else -1)
    elif cmd == "back":
        print(arr[-1] if arr else -1)
