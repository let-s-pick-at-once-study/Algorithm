# 153468	1508
from sys import stdin
n = int(stdin.readline()) # 4
seq = list(map(int, stdin.readline().split())) # 3 5 2 7
result_ls = [-1] * n # 오큰수 못찾았을 경우에 대비하여 초기값 -1로 세팅
stack = [] # stack에는 값이 아닌 인덱스값 할당

for i in range(n):
    while stack and seq[stack[-1]] < seq[i]: # 빈 스택X & 스택 최상위 값(seq[stack[-1]])보다 오른쪽 수인 인덱스 i 값(seq[i])이 더 크면
        result_ls[stack.pop()] = seq[i] # 오큰수를 해당 인덱스에 할당 & 오큰수 찾았으므로 스택에서 pop
    stack.append(i)

[ print(x, end = " ") for x in result_ls ] # 5 7 7 -1
