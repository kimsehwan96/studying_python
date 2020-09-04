N, K = list(map(int, input().split(' ')))
thing_list = []
for _ in range(N):
    W, V = list(map(int, input().split(' ')))
    thing_list.append((W,V))

# K는 준서가 버틸 수 있는 무게 1 ~ 100,000
# 각 물건은 무게가 1 ~ 100,000이고, 가치는 0~1,000이다.
#배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

