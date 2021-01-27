# 28968	96
from sys import stdin

str = stdin.readline().strip()
result = ""
word = ""
# 단어를 뒤집어야 하는지 아닌지 알려주는 플래그 변수 (기본값이 true)
reverse = True

for letter in str:
    # "<"가 나오면 단어를 뒤집으면 안됨
    if letter == "<":
        reverse = False
        # "<"를 만났을 때 이전까지 word에 축적되어있던 문자를 뒤집어서 출력해주고 word는 다시 초기화
        result += word[::-1] + letter
        word = ""
    
    # ">"가 나오면 그다음 오게될 문자부터는 단어를 뒤집어야 함
    elif letter == ">":
        reverse = True
        result += letter
    
    # 뒤집으면 안되는 경우(괄호 안에 있는 경우)에는 result에 해당 문자를 바로 축적
    elif not reverse:
        result += letter
    
    # 뒤집어야 하는 경우(괄호 밖에 있는 경우)에는 단어별로 뒤집어야 하기 때문에 word라는 새로운 변수에 해당 문자 할당
    elif reverse:
        # 빈칸을 만났다는 것은 하나의 단어가 완성되었다는 뜻 -> result에 word를 뒤에서부터 반대로 출력해주고, word는 다시 초기화
        if letter == " ":
            result += word[::-1] + " "
            word = ""
        else:
            word += letter

# 마지막까지 처리되지 못한 경우(단어가 "<"를 만나지 못하고 끝난 경우) 처리
result += word[::-1]
print(result)
