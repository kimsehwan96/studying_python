def finding_sum(N, M):
    #N 카드의 개수
    #M 카드 3장의 합
    #세장을 모두 더해서 어레이에 저장한다.
    #M과 가장 가까운 3장의 합을 출력한다.
    pass

if __name__ == "__main__":
    N, M = list(map(int, input().split(' ')))
    cards = list(map(int, input().split(' ')))

    result = 0
    length = len(cards)

    count = 0
    for i in range(0, length):
        for j in range(i + 1, length):
            for k in range(j +1, length):
                sum_value = cards[i] + cards[j] + cards[k]
                if sum_value <= M:
                    result = max(result, sum_value)
    
    print(result)