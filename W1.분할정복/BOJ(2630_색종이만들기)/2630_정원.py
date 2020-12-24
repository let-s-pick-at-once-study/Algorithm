N = int(input())
table = [list(map(int, input().split(" "))) for _ in range(N)]
count_white, count_blue = 0, 0

def cut(n, x, y):
    global count_white, count_blue
    check = table[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != table[i][j]:
                # 4분할로 나누기
                cut(n//2, x, y) # 1사분면
                cut(n//2, x + n//2, y) # 2사분면
                cut(n//2, x, y + n//2) # 3사분면
                cut(n//2, x + n//2, y + n//2) # 4분면
                return
		
    if check == 0:
        count_white += 1
        return
    else:
        count_blue += 1
        return

def solution(n):
    cut(n, 0, 0)
    print("%s\n%s" %(count_white, count_blue))

solution(N)
