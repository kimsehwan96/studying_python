
#중첩된 리스트


a = [1,2,3,['a','b','c']]

print(a[-1]) #바깥쪽 배열의 인덱스 0의 값은 1, 1의 값은 2, 2의 값은 3, 3의 값은 또다른 리스트이다.
# [-1] 인덱스는 배열의 마지막 요소를 나타날때 많이 사용한다.

print(a[-1][0])
