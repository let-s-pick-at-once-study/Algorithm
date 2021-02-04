# 메모리 초과
from sys import stdin
from functools import reduce

n,r = map(int, stdin.readline().split())
r = min(r, n-r)
5 2 -? [5,4,3]
numerator = reduce((lambda x,y: x*y), list(range(n, n-r, -1)))
denominator = reduce((lambda x,y: x*y), list(range(1, r+1)))
result = numerator // denominator
count = 0

for x in str(result)[::-1]:
    if x != "0":
        break
    else:
        count += 1

print(count)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 28776	84
from sys import stdin

n,r = map(int, stdin.readline().split())

def count_element(M, num):
    count = 0
    divnum = num
    while M >= divnum:
        count += (M // divnum)
        divnum *= num
    return count

print(min(count_element(n,5) - (count_element(r,5) + count_element(n-r,5)),
          count_element(n,2) - (count_element(r,2) + count_element(n-r,2))))
