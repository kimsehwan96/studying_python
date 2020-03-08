test_case_num = int(input())

#lists = ['O','O','X','X','O','O','X','X','O','O']

#print(lists)

#print(len(lists))



for x in range(test_case_num):
    lists = input()
    check_before = 0 # 전에 나온 문자가 O면 1, 아니면 0
    sum = 0 # 점수들의 합
    score_ac = 1#연쇽으로 나올 떄 마다 증가하는 점수

    for x in range(len(lists)):
        if lists[x] == "O":
            if check_before == 1:
                score_ac = score_ac + 1
                sum = sum + score_ac



            else:
                score_ac = 1
                sum = sum + 1
                check_before = 1


        else:
            check_before = 0
            score_ac = 1

    lists=[]
    print(sum)
    sum = 0
