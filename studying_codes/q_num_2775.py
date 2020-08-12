# 0층의 i호에는 i명이 산다. 
# 01호 1명, 02호 2명 
'''
1명 4명 10명 20 35 56 84  110          2층   floor[2]
1명 3명 6명 10명 15 21 28 36     1층  floor[1]
1명 2명 3명 4명 5명 6명 7명 8명 ... 0층  floor[0]
'''
def zero_floor_table(n):
    table = []
    for i in range(n):
        table.append(i+1)
    return table

def calculate(k, n):
    # k는 층수, n은 호수
    floor = []
    tmp_list = []
    floor.append(zero_floor_table(n))
    for idx in range(k):
        floor.append([])
        for i in range(n):









if __name__ == "__main__":
    testNum = int(input())
    calculate(1,3)