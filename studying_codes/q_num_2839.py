
def fiveAndthree(weight):
    divm = divmod(weight,5)
    w_5 = divm[0] # 5kg 봉지 개수 총 18키로그램일경우 3.
    res = divm[1] # 3키로그램 봉지로 채워야하는 무게 총18그램일경우 3키로
    if res % 3 != 0:
        return -1
    else:
        w_3 = res // 3
        sum = w_5 + w_3
        return sum
    
def three(weight):
    if weight % 3 != 0:
        return -1
    else:
        w_3 = weight // 3
        return w_3

#def threeAndfive(weight):



# this is main
# input 이 11인 경우가 에러 발생.
# 11이면 3키로그램 2개, 5키로그램 1개로 적용이 된다. 
# 즉 3키로그램부터 채우고 5키로그램을 채우는 로직도 추가해야겠네.. 어떻게 보면 예외인가? 5키로그램을 한번만 채우는 경우가 있을탠데



num = int(input())
a = fiveAndthree(num)
b = three(num)

if (a == -1) & (b == -1):
    print("-1")
else:
    if (a == -1):
        print(b)
    elif (b == -1):
        print(a)
    else:
        if a > b:
            print(b)
        else:
            print(a)



# 3kg 봉지만 채웠을 때의 경우와

# 3kg봉지와 5kg 봉지를 채웠을 때의 경우를 비교해서, 더 적은 쪽을 출력해야겠네.