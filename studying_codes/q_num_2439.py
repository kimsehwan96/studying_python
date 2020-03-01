n= int(input())
cnt = 0

for x in range(n):
    cnt += 1
    for x in range(n-cnt):
        print(' ' ,end='')
    for x in range(cnt):
        print('*', end='')
    print('')


#  별찍기 쉽지않네..

# 공백 공백 공백 공백 별
# 공백 공백 공백 별 별
# 이런식으로 가야하니까..
