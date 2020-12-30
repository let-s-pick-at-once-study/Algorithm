# 10972_다음순열
# 메모리 초과 => N!만큼 순열을 구해야하기 때문에 시간복잡도가 매우 크다
import itertools
permutations = itertools.permutations

N = int(input())
ls = list(permutations(list(range(1, N+1))))
check = tuple(map(int, input().split()))


for idx, element in enumerate(ls):
    if element == check:
        if idx == (len(ls)-1):
            print(-1)
            break
        else:
            print(str(ls[idx+1]).replace("(","").replace(")","").replace(",",""))
            break
            
------------------------------------------------------------------------------------
# 29840KB 72ms
T = int(input()) # 1 <= T <= 10,000
list = list(map(int, input().split()))

def solution(ls):
    if T == 1: # T=1인 경우 처리 안해주면, 런타임에러
        return [-1]
    for i in range(T-1, 0, -1):
        if ls[i] < ls[i-1]:
            break
    if i == 1 and ls[i] > ls[i-1]: # 입력받은 리스트가 가장 작은 값일 경우
        return [-1]
    for j in range(T-1, i-1, -1):
        if ls[j] < ls[i-1]:
            break

    ls[i-1], ls[j] = ls[j], ls[i-1] 
    return ls[:i] + sorted(ls[i:], reverse=True) # 

print(" ".join(map(str, solution(list))))
