# 68ms 29076KB
T = int(input())

for _ in range(T):
    N = int(input())
    result = [1, 2, 4]

    for i in range(3, N):
        result.append(result[i - 3] + result[i - 2] + result[i - 1])

    print(result[N - 1])
    
---------------------------------------------------------------------------------------------------------------------

# 64ms 29076KB
# T번의 입력을 받으면서 매번 result를 계산하지 않고, 우선 result를 구해놓은 다음 해당 인덱스 출력만 하도록 refactoring(N<11) -> 4ms의 이득
T = int(input())
result = [1, 2, 4]
for i in range(3, 10):
    result.append(result[i-3] + result[i-2] + result[i-1])

for _ in range(T):
    N = int(input())
    print(result[N - 1])
