# 28776	64
from sys import stdin
num = int(stdin.readline())
div = 2

while div * div <= num:
  if num % div == 0:
    print(div)
    num //= div
  else:
    div += 1

if num > 1:
  print(num)
