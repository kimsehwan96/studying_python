import sys

try:
    while 1:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
except:exit()


## 백준 eof 문제. 예외가 발생할때는 종료시키는 코드를 추가해야 한다.
