# 시간초과
from sys import stdin

bin_num = stdin.readline().strip()
decimal_num = 0
octal_num = ""

# 2진수에서 10진수
multiplier = 1
for x in bin_num[::-1]:
    if x == "1":
        decimal_num += multiplier
    multiplier *= 2

# 10진수에서 8진수
while decimal_num >= 8:
    octal_num += str(decimal_num % 8)
    decimal_num //= 8
octal_num += str(decimal_num)

print(octal_num[::-1])

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

# 30292	80
from sys import stdin

# 입력받은 이진수 문자를 십진수로 변환
decimal_num = int(stdin.readline(), 2)
# 십진수를 8진수로 변환하여 출력
print(format(decimal_num, "o"))
