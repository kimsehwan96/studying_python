"""
입력
5
55 185
58 183
88 186
60 175
46 155

출력
2 2 1 2 5
"""
import sys

def find_rank(infos:list):
    ranking = []
    for v in infos:
        rank = 1
        w = v[0]
        h = v[1]
        for v_c in infos:
            if v_c == v:
                continue
            else:
                w_comp = v_c[0]
                h_comp = v_c[1]
                if ((w < w_comp) & (h < h_comp)):
                    rank += 1
                else:
                    pass
        ranking.append(rank)
    return ranking


if __name__ == "__main__":
    infos = []
    dc = [] #dc[0] = weight, dc=[1] = height
    test_case =  int(input())
    for _ in range(test_case):
        dc = list(map(int, input().split(" ")))
        infos.append(dc)
    
    ranking = find_rank(infos)
    for _ in ranking:
        print( _ , end = ' ')