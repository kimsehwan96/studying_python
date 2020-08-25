def make_666_table():
    six_list = []
    for i in range(3000000):
        if str(i).count('666') >= 1:
            six_list.append(i)
    return six_list
# 666 1666 2666 3666 4666 5666 6666 7666 8666 9666 6661
# 6662 6663 6664 6665 6666 6667 6668 6669 6660 

# 규칙 1~숫자 + 666
# 666 + 0~숫자
# 겹치는 경우? 

# 앞에 6 + 666
# 뒤에 666 + 6 
# 이 때는 겹치네.



if __name__ == "__main__":
    li = make_666_table()
    li.sort()
    n = int(input())
    #print(li[n-1])
    print(li[n-1])