import sys

tc = int(sys.stdin.readline().rstrip())

#입력에 애초에 지울 수 있는 수가 있음을 보장 할 수 있다고 하니 예외처리는 불필요

stack = []

for _ in range(tc):
    n = int(sys.stdin.readline().rstrip())
    if (n == 0):
        stack.pop()
    else:
        stack.append(n)

sum = 0

for v in stack:
    sum += v

print(sum)
