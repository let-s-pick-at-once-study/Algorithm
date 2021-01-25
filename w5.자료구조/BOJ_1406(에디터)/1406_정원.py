from sys import stdin

stack1 = list(stdin.readline().rstrip())
stack2 = []

for _ in range(int(stdin.readline())):
		# 명령어(cmd)와 값(value)을 리스트 형태로 저장
    input = stdin.readline().split()
    cmd = input[0]

		# L: 커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
    if cmd == "L":
				# stack1이 비었다는 것은 문장 맨 앞이라는 의미
        if stack1: stack2.append(stack1.pop())
        else: continue
		# D:	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
    elif cmd == "D":
				# stack2가 비었다는 것은 문장 맨 뒤라는 의미
        if stack2: stack1.append(stack2.pop())
        else: continue
		# B:	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
    elif cmd == "B":
        if stack1: stack1.pop()
        else: continue
		# P $: $라는 문자를 커서 왼쪽에 추가
    elif cmd == "P":
        stack1.append(input[1])

# stack2에는 stack1에서 추출한 문자를 append한 것이기 때문에, 출력할 때는 반대방향으로 출력해주어야 함
print("".join(stack1 + list(reversed(stack2))))
