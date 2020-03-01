n = 0

lists =[]
lists.clear()

while True:
    tmp = int(input())
    lists.append(tmp)
    n += 1
    if n == 9:
        break
    else:
        pass

lists_compare = lists.copy()
#입력이 틀린 생각이였네 한줄에 하나씩 읽고 리슽트에 추가해야 되니까
#에러나는 이유... 리스트_1 = 리스트_2 ->이건 객체가 아예 동일해진다
# 동일한 메모리를 참조하게 되니까. 지금처럼ㅁ 복사를 하고 싶다면
# copy()메소드를 써야할 것 같다.
lists_compare.sort()

#최댓값 은 lists_compare[8] 에 저장이 되어있다.
# 이 값의 인덱스를 찾으면 되겠지.
#최댓값은 lists_compare[8] 에 위치한다. 따라서

print("%d" %(lists_compare[8]))
print("%d" %(lists.index(lists_compare[8]) + 1 ))
