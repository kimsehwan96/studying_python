#range 함수는 일정 범위의 수를 반환한다고 해요

# range(b) -> 0부터 b-1까지의 수를 반환한다
# range(a,b) -> a부터 b-1까지의 수를 반환한다.

#range(a,b,n) -> a부터 b-1까지의 n간격의 수를 반환한대요



A = range(5)

print(type(A))

print(A)

B = list(range(5))
print(B)

C = list(A)
print(C)

print(list(range(5)))
print(list(range(5,10)))
print(list(range(3,10,2)))
print(list(range(3,10,-2)))
# 마지막 값은 n간격의 수인데, 음수 간격의 수는 없나보다 3~10까지에서

print(list(range(10,1,-2)))

print(list(range(10,1)))

#단순히 큰 값에서 작은값을 레인지 잡으면 출력이 안되고, 음수 간격을 줘야
#출력이 된다!
