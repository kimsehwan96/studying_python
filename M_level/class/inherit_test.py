# 상속 및 다중 상속

# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식클래스) -> 모든 속성, 메소드 사용 가능

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 부모
# 상속 받아서, 물려받아서 사용하고, 나머지것들은 자식 클래스에서 구현해서 사용

class Car:
    """Parent Class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method !"'
    
class BmwCar(Car):
    """ Sub class"""
    def __init__(self, car_name, tp, color): ##tp와 color는 부모 클래스에 넘겨줄거
        super().__init__(tp, color) #부모클래스의 생성자 호출
        self.car_name = car_name
    
    def show_model(self) -> str:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car):
    """ Sub class"""
    def __init__(self, car_name, tp, color): ##tp와 color는 부모 클래스에 넘겨줄거
        super().__init__(tp, color) #부모클래스의 생성자 호출
        self.car_name = car_name
    
    def show_model(self) -> str:
        return "Your Car Name : %s" % self.car_name

    def show(self): #부모에게도 있는 메서드이므로 BenzCar 의 인스턴스에서 이놈을 실행하면, 서브 클래스의 show 메서드 구현 부가 실행
        print(super().show()) # 부모 클래스의 show()메서드
        return 'car Info : %s %s %s' % (self.car_name, self.type, self.color)

#일반적인 사용

model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) #sub class에는 없지만, 부모클래스에 있는 속성
print(model1.type) # 부모클래스에 있던 속성
print(model1.car_name) # 서브 클래스에서 정의한 속성
print(model1.show()) # 부모 클래스의 메서드
print(model1.show_model()) # 서브 클래스의 메서드
print(model1.__dict__) # 부모 클래스의 인스턴스 변수 선언한거 (그리고 생성시 초기화한거)랑, 서브 클래스에서 초기화한 인스턴스 변수 모두 보임

# Method overriding

model2 = BenzCar('220d', 'suv', 'black')
print(model2.show()) # 서브 클래스에 구현된 show 메서드가 호출됨

# Parent Method Call

model3 = BenzCar('350s', 'sedan', 'silver')
print(model3.show()) #부모 메서드를 여기서 호출하는 방법?!!! 내가 짱 궁금해 했던거다. 아 그게아니고, 오버라이딩한 메서드에서 부모 클래스접근하는거네 ㅠ

# Inheritance Info

print(BmwCar.mro()) ## 상속 관계 확인하는 메서드.


# 다중 상속

class X(object):
    pass

class Y:
    pass

class Z():
    pass

class A(X, Y): #A 클래스는 X와 Y를 상속 받겠다.
    pass 

class B(Y, Z): #B 클래스는 Y와 Z를 상속 받는다.
    pass


class M(B, A, Z): #M 클래스는 B, A, Z를 상속받는다.
    pass

print(M.mro())

'''
[<class '__main__.M'>, 
<class '__main__.B'>,
 <class '__main__.A'>,
  <class '__main__.X'>,
   <class '__main__.Y'>, 
   <class '__main__.Z'>, 
   <class 'object'>]
'''