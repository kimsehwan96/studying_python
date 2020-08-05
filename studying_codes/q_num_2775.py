# 0층의 i호에는 i명이 산다. 
# 01호 1명, 02호 2명 
'''
3명 8명 15명 29            2층 
2명 3명 6명 10명 15 21 28 36     1층 
1명 2명 3명 4명 5명 6명 7명 8명 ... 0층 
'''

#테이블을 먼저 만들어서 처리? 

root = {}
# {'1' : [] , '2' : [] , '3', []} 

#k층 n호
def make_table(k, n):
    root[0] = [x+1 for x in range(n)]
    for idx in range(k):
        root[idx+1] = []
        for n in range(n):
            
            #root[idx+1].append()
    



if __name__ == "__main__":
    #numTest = int(input())