# 28776	68
from sys import stdin

input = stdin.readline().rstrip()
result = ""

# 소문자/대문자 배열 만들기
lower = list(map(chr, list(range(ord("a"), ord("z")+1)))) # [a,b,c,d, ... ,y,z]
upper = list(map(chr, list(range(ord("A"), ord("Z")+1)))) # [A,B,C,D, ... ,Y,Z]

for c in input:
    # 숫자이거나 공백인 경우
    if c.isdigit() or c == " ":
        result += c
    # 소문자인 경우
    elif c.islower():
        result += lower[(lower.index(c) + 13) % 26]
    # 대문자인 경우
    else:
        result += upper[(upper.index(c) + 13) % 26]
print(result)
