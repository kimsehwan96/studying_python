
수열의개수,한계정수 = map(int,input().split())

#수열의개수 = int(input())
#한계정수 = 5
count = 0

# 수열의 개수를 입력받고, 한계 정수도 입력받는다(이 정수보다 낮은
# 값들을 출력할거다

#그리고 리스트를 입력받는다.

lists = list(map(int,input().split()))

#입력을 받는다잉
# lists에는 10개의 원소가 존재하게 된다.

for x in range(수열의개수):
    if lists[count]<한계정수:
        print(lists[count], end=' ')
        count += 1
    else:
        count += 1
