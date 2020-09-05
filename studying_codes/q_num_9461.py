# 파도 반 수열
# 1  2  3  4  5  6  7  8  9  10 11 # index
# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9 12
# 보니까 P(N) = P(N-1) + P(N-5) 같은디?
# 맞는듯.
dp = [x for x in range(101)]
#dp[0] 은 사용 안할거임.
dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2
dp[6] = 3

TestNum = int(input())

for _ in range(TestNum):
    N = int(input())
    if N <= 7:
        print(dp[N])
    else:
        for i in range(7, 101):
            dp[i] = dp[i-1] + dp[i-5]
        print(dp[N])

