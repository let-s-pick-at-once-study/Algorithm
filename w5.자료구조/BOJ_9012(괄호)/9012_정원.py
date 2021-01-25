# 28776KB	64ms
from sys import stdin

def solve(list):
    # 비어있는 스택 생성
    stack = []
    
    for x in list:
        if x == "(":
            stack.append(x)
        else:
            try:
                stack.pop()
	    # 스택이 비어있어서 pop할 수 없는 경우 (예외처리)
            except:
                return "NO"

    return "YES" if len(stack) == 0 else "NO"


for _ in range(int(stdin.readline())):
    ls = [x for x in stdin.readline().rstrip()]

    print(solve(ls))
