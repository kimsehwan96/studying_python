import math

def find_days(n:list):
    A = n[0]
    B = n[1]
    V = n[2]
    days = math.ceil((V - A)/(A-B)) + 1
    print(days)

if __name__ == "__main__":
    n = list(map(int , input().split(' '))) #[1,2,3]
    find_days(n)

# 맞은 코드이지만, 반례를 확인해서 복습 할 필요가 있음
# 이분 탐색 