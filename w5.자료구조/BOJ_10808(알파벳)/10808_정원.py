# 28776	64
from sys import stdin
input = stdin.readline().strip()


# alpha_dict = { "a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0,
#                "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0 }

alpha_dict = {}
# ord() : 문자의 아스키 코드 값을 출력해주는 함수
# chr() : 아스키 코드 값(숫자)을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
for key in range(ord("a"), ord("z")+1):
    alpha_dict[chr(key)] = 0

for letter in input:
    alpha_dict[letter] += 1

print(" ".join(list(map(str, alpha_dict.values()))))
