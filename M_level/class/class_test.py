# 파이썬 클래스 한번 다시 정리

# Self, 클래스, 인스턴스 변수

# 선언

class UserInfo:
    #속성, 메소드
    def __init__(self, name):
        self.name = name
        self.age = 5
    
    def user_info_p(self):
        print("Name : ", self.name)

user1 = UserInfo("kim")
user1.user_info_p()

print(user1.__dict__) #user1 인스턴스의 네임스페이스에 저장된 인스턴스 변수들을 딕셔러니 형태로 확인 가능


# 클래스와 인스턴스의 차이를 이해하는것 중요 OK
# 네임 스페이스 : 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성 가능
# 인스턴스 변수 : 객체마다 별도 생성 가능, 인스턴스 생성 후 사용한다.


class SelfTest(object):

    def function1(): #self 인자가 없어서 누구의 함수인지 알 수가 없다. 이건 클래스 메소드다.
        print('function1 called')
    def function2(self):
        print(id(self))
        print('function2 called')

self_test = SelfTest()
# self_test.function1() #에러가 난다.

SelfTest.function1()
self_test.function2()
# SelfTest.function2() #error
SelfTest.function2(self_test) #정상.


# 클래스 변수, 인스턴스 변수
# 클래스 변수 self 없이, 인스턴스 변수 self

class WareHouse:
    # 클래스 변수, 여러 인스턴스에서 공유한다.
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1 #클래스 변수를 하나씩 증가해준다, 인스턴스가 생길 떄 마다

    def __del__(self):
        WareHouse.stock_num -= 1 #클래스 변수를 하나씩 감소해준다, 인스턴스가 생길 떄 마다

user1 = WareHouse('kim')
user2 = WareHouse('park')
user3 = WareHouse('lee')

print(user1.__dict__) #인스턴스 변수만 출력된다. 해당 인스턴스의 네임스페이스
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__)
'''
{'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x7fc8980a1cb0>, 
'__del__': <function WareHouse.__del__ at 0x7fc8980a1560>, 
'__dict__': <attribute '__dict__' of 'WareHouse' objects>, 
'__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, 
'__doc__': None}
'''

#위와 같이 나온다 출력. stock_num이 3이 되었다, 모든 인스턴스가 클래스 변수를 공유했기 떄문에.

print(user1.stock_num) #자기 namespace에 stock_num은 없지만, 없을 경우 클래스의 네임스페이스를 가서 찾고, 이 때도 없다면 오류

del user1
print(user2.stock_num) #user1의 소멸자에 클래스 변수 stock_num을 빼버렸기 때문에 user2.stock_num 은 2가 출력된다. (클래스 네임스페이스에 있는 값이 2가 되었다)
