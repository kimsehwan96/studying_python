


A = [1,2,3,4]
#A는 리스트
B = (1,3,5)
#B는 튜플
C = {2,4,6,8,10}
#C는 집합
D = {1:90, 2:88, 3:93}
# D는 사전형

E =tuple(A)
print(E)
#F = dict(A)
#print(F)
#TypeError: cannot convert dictionary update sequence element #0 to a sequence
# 변환 할 수 없다고 나오는데?
# 키 : 값 쌍이 없으면 변환이 안되나바

G = list(D)

print(G)

# 사전을 리스트로 변환하면 키값만 뽑혀 나온다.

c = D.values()

print(c)

print(type(c))

# D.values() 했을때는 사전의 값만 뽑히는데, 이걸 변수에 넣으면
# 클래스 타입이 dict_values 로 나오넹.

f = list(c)

print(f)

# 만약에 사전 형 데이터의 값들을 리스트로 만들고 싶다면 ?
# 위의 코드를 참조하면 되겠지?
