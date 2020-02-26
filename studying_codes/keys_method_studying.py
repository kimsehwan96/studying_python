
score = {1:90, 2:80, 3:80, 4:20, 5:52}

# 사전 score는 학생번호:성적으로 구성했다.

for x in score:
    print(x)

for x in score.keys():
    print(x)

for x in score.items():
    print(x)
#출력값을 보니까 튜플로 반환 된 것 같네요



for x,y in score.items():
    print(x,y)
# **** 사전에서 키와 값을 따로 따로 얻어 낼 때 좋은 것 같은데?
#정확한 활용법은 더 연구해봐야 할 듯.

# 이렇게 하니까 x랑 y 따로 입력이 들어 갔쥬?
# 사전형데이터셋.items() 는 키와 값을 가져오는 것 같아요


dicts = {1:10 ,2:20, 3:30}

a,b,c = dicts.items()

print(a)
print(b)
print(c)

# dicts의 키:값 쌍을 얻어왔어요. 좀 이해하기 어렵네요
# a,b,c = dicts.items()를 하니까 a에 키,값 쌍이 튜플로 들어 온 듯?
print(type(a))

#확인해보니 맞네요 튜플로 들어왔어요.



for x in score.values():
    print(x)

# values() 메소드를 사용하니까 값들이 얻어 졌어요
# keys() 메소드는 아까 키를 얻어 왔잖아요
