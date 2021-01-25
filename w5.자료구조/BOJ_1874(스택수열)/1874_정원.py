#31404KB	168ms
from sys import stdin

# 함수가 호출될 때마다 초기화되면 안되고 계속 값이 저장된 상태여야 하므로 전역변수로
stack, signs = [], []
# 1부터 n까지의 수를 대변하는 변수
num = 1

def solve(target):
		# global은 전역 변수를 변경하거나 할당하는 경우에만 써주면 됨    
		global num, signs
		
    # target 숫자까지 스택에 num을 쌓아줌 & "+"기호 append
    while num <= target:
        stack.append(num)
        signs.append("+")
        num += 1

    # 스택에 쌓인 마지막 숫자와 target값이 같다면 스택에서 빼줌 & "-"기호 append
    if target == stack[-1]:
        stack.pop()
        signs.append("-")
    else:
        # 위의 조건을 만족하지 않으면 signs배열을 초기화 & False return
        # signs배열을 함수 내에서 초기화시키고 있기 때문에 global화 해주어야 함
        signs = []
        return False

    return True


# 입력받는 부분 - 한줄씩 읽어가면서 그때마다 solve 함수를 호출하는 방식
for _ in range(int(stdin.readline())):
    target = int(stdin.readline())

    # 조건을 만족하지 않으면 target을 더이상 읽어들이지 않고 스톱
    if not solve(target):
        break


# 스택수열을 만들수 없는 경우는 signs가 빈 배열일 것 
# 정상적이라면 비어있지 않을 것이라는 조건을 활용해 출력
( print("\n".join(signs)) if len(signs) != 0 else print("NO") )
