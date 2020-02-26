# 첫줄에 정수 입력을 2개 받아 첫줄에 두 정수의 합을 출력


# 내가 생각한 코드
# a = int(input())
# b = int(input())
# print(a+b)


#정답코드

a, b = map(int, input().split())
print(a+b)



# ex ) a,b =1,2
# a=1, b=2 임을 기억하자.

# map 함수는 어떻게 동작 ?
# list나, dictionary같은 iterable 한 데이터를 인자로 받아
# list 안의 개별 item을 함수의 인자로 전달
# 즉 input().split()을 했을때
# 1 2를 입력으로 넣으면 ['1','2'] 로 리스트 화 되는데
# 이 각각의 '1' 과 '2'를 int 함수에 넣는 것이다.

# 사칙연산 문제들은 이와 같은 방법으로 해결
