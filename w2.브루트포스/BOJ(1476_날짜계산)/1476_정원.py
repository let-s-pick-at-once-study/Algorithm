# 시간초과
E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
count = 1
while (True):
    if e > 15:
        e = 1
    if s > 29:
        s = 1
    if m > 20:
        m = 1

    if e == E and s == S and m == M:
        break

    count += 1
    e+=1; s+=1; m+=1

print(count)

-------------------------------------------

E, S, M = map(int, input().split())

def search(E, S, M):
    e, s, m = 1, 1, 1
    count = 1
    for i in range(15*28*19):
        if e == E and s == S and m == M:
            return count
        e = e+1 if e < 15 else 1
        s = s+1 if s < 28 else 1
        m = m+1 if m < 19 else 1
        count += 1

print(search(E, S, M))
