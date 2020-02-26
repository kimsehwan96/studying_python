lists=[1,2,3]

#리스트 안의 원소(객체) 개수는 3개다.

print(lists)
print(type(lists))

for a in lists:
    print("원소 개수가 몇개일까용")
    print(a)

# 원소의 개수만큼 반복이 되었다.

for a in lists:
    a+=1
    print("몰까용")
    print(a)

# a의 값과는 무관하게, 데이터 집합 안의 원소 개수만큼 작업이 일어나는 것 같아용
# 데이터 집합에서 데이터를 하나씩 변수 a에 넣고 반복을 수행하네요

strs="안녕하세용"
print(strs)

for x in strs:
    print("원소 개수 몇개일까용")
#문자열 안에 원소 개수 5개 만큼 출력이 되었네요

for x in range(5):
    print(x)

# 아하 보통 몇개만큼 반복된 작업을 해야 한다면(반복 횟수는 우리가
#정하는 수치라면, range 함수를 이용하면 되겠네요.

print(list(range(1,10,2)))
for data in range(1,10,2):
    print(data+1)


for letter in strs:
    print(letter)

for alpha in 'songang':
    y = alpha.upper()
    print(y)

# 이런식으로 어떤 데이터 집합 안에 있는 것들을 원소 하나하나
#처리 할 때도 유용하겠네요

#구구단을 한번 짜볼까요
