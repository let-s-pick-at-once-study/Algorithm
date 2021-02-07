# 44396	2748
from sys import stdin

t = int(stdin.readline())
nums = [int(stdin.readline()) for _ in range(t)]
# 입력받는 수 중 가장 큰 수 만큼의 소수 판별 리스트를 만들어 놓으면 다른 수들에서는 언제나 사용 가능
m = max(nums)

def check_prime(m):
		# 인덱스와 요소 자리를 맞춰주기 위해 [False,False] 추가(0과 1자리)
    isPrime = [False,False] + [True] * (m-1)
    for i in range(2, int(m**0.5)+1):
        if isPrime[i]:
            for j in range(i*i, m+1, i):
                isPrime[j] = False
    return isPrime

# 소수 판별 리스트
prime_list = check_prime(m)

for num in nums:
    count = 0
		# 0과 1은 소수가 아니므로, 2부터 확인
		# 중복을 허용하지 않으므로 num의 절반의 수까지만 확인
    for value in range(2, num//2 + 1):
        if prime_list[value] and prime_list[num-value]:
            count += 1
    print(count)
