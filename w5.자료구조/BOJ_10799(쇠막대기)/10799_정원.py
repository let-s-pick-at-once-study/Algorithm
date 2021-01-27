# 29304	80
from sys import stdin

# 레이저가 나오는 부분을 X로 문자열 변경
input = stdin.readline().replace("()", "X")

stack = []
# 쇠 막대기 개수
count = 0
# 잘린 쇠막대기 토막의 개수
cut = 0

for c in input:
    if c == "(":
        stack.append(c)
        count += 1
    elif c == ")":
        stack.pop()
    # 레이저로 인해 막대기가 잘리는 경우
    else:
        # 현재 스택에 남아있는 원소들의 개수만큼 잘린 토막이 생겨난다
        cut += len(stack)

# 토막 개수 + 쇠 막대기 개수
print(cut + count)
