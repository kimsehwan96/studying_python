#입력된 세 수중 두번쨰로 큰 정수를 출력하는 프로그램 작성



#if 문제이니까 if만 쓰겠습니다. 사실 list.sort()를 쓰면 될...것,.같..
# 백준 내에서 입력
a,b,c = map(int, input().split())

if a>b:
    tmp = a
    a = b
    b = tmp
else:
    pass

if b>c:
    tmp = b
    b = c
    c = tmp
else:
    pass

if a>b:
    tmp = a
    a = b
    b = tmp
else:
    pass

print(b)


#맞았당
