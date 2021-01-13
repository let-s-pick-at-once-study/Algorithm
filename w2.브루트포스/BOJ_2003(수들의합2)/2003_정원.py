# 29540KB	68ms
# 시간복잡도는 summary와 m을 비교하는 횟수 / start와 end 포인터가 움직인 횟수(최대로 움직여봤자 2N번)
# O(N)의 시간복잡도
import sys

# N은 데이터 개수 / M은 찾고자 하는 부분합 
N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
end = 0
interval_sum = 0

# start를 차례로 증가시키면서 반복
for start in range(N):

    # end를 가능한 만큼 이동시키기
    while interval_sum < M and end < N:
        interval_sum += arr[end]
        end += 1

    # 부분합이 M이면 카운트 증가
    if interval_sum == M:
        count += 1

    # 다음 차례를 위해 현재 start위치에 있는 값을 부분합에서 빼줌
    interval_sum -= arr[start]

print(count) 
