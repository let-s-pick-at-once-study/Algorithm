# N과 M(1)

https://hjp845.tistory.com/77

- 런타임 에러

```python
# input
N, M = map(int,input().split())

check = [False for i in range(N+1)] #조합 사용 표시 list
subs = [i for i in range(m)] #뽑을 m개 list

def go(idx,n,m):
    if idx==m: #m개 모두 뽑으면 반환
        print(' '.join(map(str,subs)))
        return
    else:
        for i in range(1, n+1):
            if check[i]==False:
                check[i]=True
                subs[idx]=i
                go(idx+1, n,m)
                check[i]=False
    
go(0,N,M)    
```

- combination 사용

```python
# input
N, M = map(int,input().split())

from itertools import combinations
nlist = list(range(1,N+1))
comb = sorted(combinations(nlist,M))

for c in comb:
    print(' '.join(map(str,c)))

```

