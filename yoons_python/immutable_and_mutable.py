

# immutable 객체는 수정 불가능한 객체. mutable 객체는 수정 가능한 객체이다.

r = [1,2]

print("r = [1,2]에서 r의 주소는 : {}".format(id(r)))

r += [3,4] #리스트에 값을 추가한다.

print("수정된 r은 {}".format(r))

print("수정된 r의 주소는 {}".format(id(r)))

# 리스트의 주소는 동일하다.
# 리스트는 mutable한 객체

t = (1,2) #튜플

print("t = (1, 2) 의 주소 {}".format(id(t)))
tmp_1 = id(t)

t += (3,4)

print("수정된 t는 {}".format(t))

print("수정된 튜플 객체의 주소는 {}".format(id(t)))
tmp_2 = id(t)

print("기존 튜플 객체의 주소와 바뀐 튜플 객체의 주소가 동일한가요 : {}".format(tmp_1 == tmp_2 ))

# 튜플 객체는 immutable이다. 즉 세로운 튜플이 만들어 진 것이다. (수정된것이 아니라는 의미)

def add_last(m,n):
    m += n

# 위 함수는 리스트에 값을 추가하기 위해 임시로 만든 함수이다. 

r = [1,2]
print("r은 : {}".format(r))
add_last(r,[3,4]) #  객체에 [3,4]를 추가함
print("add_last 함수를 통과한 r은 {}".format(r))

# 튜플에서도 작동을 할 것인가에 대해서 확인해보자.

t = (1,2)
print("t는 : {}".format(t))

add_last(t,(3,4))

print("add_last 함수를 통과한 t는 {}".format(t))

# 위 상항은 매개변수 m에 넣은 t = (1,2) 객체가 t와 m이라는 이름이 붙었다. 그러니까 (1,2)라는 객체는 변수 t와 m이 참조 하고 있다.
# n이라는 이름에는 (3,4) 가 붙었다. 
# 이 때 m += n 을 했을 때 m이라는 변수에 (1,2,3,4) 라는 튜플이 참조되고있다 하지만 t는 변한 것이 아니다.

def add_tuple(t1,t2):
    t1 += t2
    return t1 #새로 만들어진 튜플을 반환

print("this is the tuple add function")
t1 = (1,2)
t2 = (3,4)

print(" t1 : {}  t2: {} ".format(t1,t2))
print("after added")
print("{}".format(add_tuple(t1,t2)))