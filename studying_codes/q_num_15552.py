import sys


test_case_num = int(input())

for x in range(int(test_case_num)):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)


#sys.stdin.readline().split() 이친구 입력이 빠르데요...그렇다네요..
