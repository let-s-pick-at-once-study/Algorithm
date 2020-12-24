N = int(input())
# 테이블 만들기
table = [[" " for _ in range(N)] for _ in range(N)]

def solution(n):
    make_star_tree(n, 0, 0)
    print_star_tree()

# 별 그리기
def draw_star(x, y):
    global table
    table[x][y] = "*"
    table[x][y + 1] = "*"
    table[x][y + 2] = "*"
    table[x + 1][y] = "*"
    table[x + 1][y + 2] = "*"
    table[x + 2][y] = "*"
    table[x + 2][y + 1] = "*"
    table[x + 2][y + 2] = "*"

# 재귀함수(종료조건: n == 3이면 별 그리기 실행)
def make_star_tree(n, x, y):
    if n < 3:
        return
    if n == 3:
        draw_star(x, y)
        return

    make_star_tree(n // 3, x, y)
    make_star_tree(n // 3, x + n // 3, y)
    make_star_tree(n // 3, x + (2 * n) // 3, y)
    make_star_tree(n // 3, x, y + n // 3)
    make_star_tree(n // 3, x + (2 * n) // 3, y + n // 3)
    make_star_tree(n // 3, x, y + (2 * n) // 3)
    make_star_tree(n // 3, x + n // 3, y + (2 * n) // 3)
    make_star_tree(n // 3, x + (2 * n) // 3, y + (2 * n) // 3)

# 만들어진 배열 출력하기
def print_star_tree():
    for _ in table:
        print("".join(_))

solution(N)
