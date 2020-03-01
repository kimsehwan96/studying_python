n = int(input())
n_1 = n%10 # 1의 자리 수
n_10 = n//10 # 10의 자리수 (위 아래 모두 입력된 값 기준)
count = 0 #싸이클 수 측정
new_num = 0 #새로운 수
new_sum = 0 # 새로운

if n_10 == 0:
    n_10 = n_1
    n_1 = 0
    n = n_10*10 + n_1
else:
    pass

while 1:
    new_sum = n_1 + n_10
    new_num = n_1*10 + (new_sum%10)
    n_1 = new_num%10
    n_10 = new_num//10
    count = count + 1
    if new_num == n:
        break

print(count)

# 55면  싸이클은 3이 나와야 하는데
# 5+5 = 10 -> 50
# -> 5 + 0 => 5 -> 05
# -> 0 5 // 0 + 5  = 5 -> 55
#

# 0 1이면 1 0 = 1  -> 0 + 1 = 1 -> 1 1
# 1 + 1 = 2 -> 12 => 1+2 = 3 -> 23

#아니면 0 1 이면 1 0 = 1 (주어진 수는 0 1 )
