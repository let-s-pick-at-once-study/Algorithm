N = int(input())
table = [list(map(int, input())) for _ in range(N)]
result = []
count = 0

def cut(n, x, y):
    global  count
    check = table[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != table[i][j]:
                result.append("(")
                cut(n // 2, x, y)
                cut(n // 2, x, y + n // 2)
                cut(n // 2, x + n // 2, y)
                cut(n // 2, x + n // 2, y + n // 2)
                result.append(")")
                return

    if check == 1:
        result.append("1")
        return
    elif check == 0:
        result.append("0")
        return

def solution(n, x, y):
    cut(n, x, y)
    print("".join(result))

solution(N, 0, 0)
