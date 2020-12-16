house = int(input())
colors = []
for _ in house:
    costR, costG, costB = list(map(int, input().split(' ')))
    colors.append(costR, costG, costB)

dp = [x for x in range(house)]

# 빨 파 초 빨 파 초 빨 파 초
# 시작하는 색이 뭐냐가 중요한거같고.. 
# 뒤에 어떤 가격이 나올지 모르기 때문에 
# 전에 계산한 값들을 메모해놔야겠네.
# 아닌가.

for v in colors:


